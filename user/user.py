from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound
import grpc
import booking_pb2
import booking_pb2_grpc
import jwt
import datetime
from werkzeug.security import check_password_hash
from pymongo import MongoClient
from flask_cors import CORS



# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app) 

PORT = 3004
HOST = '0.0.0.0'

# Charger les utilisateurs depuis le fichier JSON
with open('{}/data/users.json'.format("."), "r") as jsf:
    users = json.load(jsf)["users"]



@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400
    uri = "mongodb+srv://Amine:23714406@cluster0.yfc0x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client.User
    collection = db["users"]  
    user = collection.find_one({"email": email})

    # Vérifier si l'utilisateur existe et si le mot de passe est correct
    if user and check_password_hash(user["password"], password):
        # Générer un token
        token = jwt.encode({
            'sub': user['id'],  # ID de l'utilisateur
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiration du token
        }, 'votre_secret', algorithm='HS256')  # Remplacez 'votre_secret' par un secret fort

        return jsonify({"token": token, "user": user["name"]}), 200
    else:
        return jsonify({"error": "Invalid email or password."}), 401





# Route pour récupérer les films via GraphQL
@app.route("/movies", methods=['GET'])
def get_movies():
    query = '''
    query {
        allMovies {
            id
            title
            director
            rating
        }
    }
    '''
    response = requests.post("http://127.0.0.1:3200/graphql", json={'query': query})
    return response.json()



@app.route("/movies/<movieId>", methods=['GET'])
def get_moviesById(movieId):  
    query = '''
    query {
        movieById(id: "%s") {
            id
            title
            director
            rating
        }
    }
    ''' % movieId  
    
    response = requests.post("http://127.0.0.1:3200/graphql", json={'query': query})
    return response.json()



@app.route("/bookings", methods=['GET'])
def get_bookings():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        bookings_dict = {}
        response = stub.GetBookings(booking_pb2.Empty())

        for booking in response:
            # Conversion des dates et des films en une liste de dictionnaires
            dates = [{"date": d.date, "movies": list(d.movies)} for d in booking.dates]
            
            # Stocker chaque réservation dans un dictionnaire avec l'ID utilisateur comme clé
            bookings_dict[booking.userid] = {
                "dates": dates
            }
    
    print(bookings_dict)
    return jsonify(bookings_dict)


from werkzeug.exceptions import NotFound

@app.route("/bookings/<userid>", methods=['GET'])
def get_bookings_byuserid(userid):
    print ("user id: ",userid)
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        response = stub.GetBookingsByUserId(booking_pb2.UserId(userid=userid))
        print(response)
        # Vérification si l'utilisateur existe
        if response.userid == "Not Found":
            
            raise NotFound("User ID not found")
        
        # Initialisation du dictionnaire des réservations
        bookings_dict = {}

        # Conversion des dates et des films en une liste de dictionnaires
        dates = [{"date": d.date, "movies": list(d.movies)} for d in response.dates]
        
        # Stocker chaque réservation dans un dictionnaire avec l'ID utilisateur comme clé
        bookings_dict[response.userid] = {
            "dates": dates
        }
    print("for the user id: ",userid)
    print(bookings_dict)
    return jsonify(bookings_dict)


@app.route("/movies/add", methods=['POST'])
def add_movie():
    data = request.get_json() 
    movie_id = data.get('id')
    title = data.get('title')
    director = data.get('director')
    rating = data.get('rating')

    # Modifiez la requête pour ne pas sélectionner d'attributs
    query = '''
    mutation {
        addMovie(id: "%s", title: "%s", director: "%s", rating: %f)
    }
    ''' % (movie_id, title, director, rating)

    try:
        response = requests.post("http://127.0.0.1:3200/graphql", json={'query': query})
        response.raise_for_status()  # Vérifie les erreurs de réponse
        return response.json()  # Retournez la réponse de l'API GraphQL
    except requests.exceptions.HTTPError as err:
        return jsonify({"error": str(err)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500






# Lancer l'application Flask
if __name__ == "__main__":
    print("Server running on port %s" % (PORT))
    app.run(host=HOST, port=PORT)
