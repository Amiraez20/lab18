import pyrebase

firebase_config = {
    "apiKey": "AIzaSyAXsK0qsx4RuLSA9C8IPSWd0eQ67HVHuJY",
    "authDomain": "firestorm-9d3db.firebaseapp.com",
    "databaseURL": "https://firestorm-9d3db-default-rtdb.firebaseio.com",
    "storageBucket": "firestorm-9d3db.appspot.com",
    "projectId": "firestorm-9d3db"
}

app = pyrebase.initialize_app(firebase_config)
auth_client = app.auth()

user_email = "TK757567@pwnsec.xyz"
recovered_password = "METTRE_ICI_LE_MDP_OBTENU_AVEC_FRIDA"

session = auth_client.sign_in_with_email_and_password(user_email, recovered_password)
print("[+] Authentification réussie.")

database = app.database()
result = database.get(session["idToken"])

print("[+] Contenu récupéré :")
print(result.val())