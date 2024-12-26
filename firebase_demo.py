import os
import pyrebase
from dotenv import load_dotenv


load_dotenv()

config = {
  "apiKey": os.getenv("API_KEY"),
  "authDomain": os.getenv("AUTH_DOMAIN"),
  "databaseURL": os.getenv("DB_URL"),
  "storageBucket": os.getenv("STORAGE_BUCKET"),
  "serviceAccount": os.getenv("SERVICE_ACCOUNT")
}

# firebase app
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# AUTH
email = "basic100@basic.com"
password = "anaaremere"
try:
    auth.create_user_with_email_and_password(email, password)
except Exception as exc:
    print(exc)
user = auth.sign_in_with_email_and_password(email, password)
user_info = auth.get_account_info(user['idToken'])

# REALTIME DB
db = firebase.database()
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)

# FIRESTORE DB
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate(os.getenv("SERVICE_ACCOUNT"))
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1816
})
doc_ref = db.collection('users').document('alovelace')
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print('No such document!')
