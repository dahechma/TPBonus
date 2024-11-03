from pymongo import MongoClient
import json
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash


uri = "mongodb+srv://Amine:23714406@cluster0.yfc0x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client.User



users_data = {
  "users": [
    {
      "id": "chris_rivers",
      "name": "Chris Rivers",
      "last_active": 1360031010
    },
    {
      "id": "peter_curley",
      "name": "Peter Curley",
      "last_active": 1360031222
    },
    {
      "id": "garret_heaton",
      "name": "Garret Heaton",
      "last_active": 1360031425
    },
    {
      "id": "michael_scott",
      "name": "Michael Scott",
      "last_active": 1360031625
    },
    {
      "id": "jim_halpert",
      "name": "Jim Halpert",
      "last_active": 1360031325
    },
    {
      "id": "pam_beesly",
      "name": "Pam Beesly",
      "last_active": 1360031225
    },
    {
      "id": "dwight_schrute",
      "name": "Dwight Schrute",
      "last_active": 1360031202
    }
  ]
}

for user in users_data["users"]:
    username = user["id"]
    user["email"] = f"{username}@example.com"  
    user["password"] = generate_password_hash("00000000")  
    
    
collection = db["users"]                   

result = collection.insert_many(users_data["users"])
print(f"Utilisateurs insérés avec succès : {result.inserted_ids}")
