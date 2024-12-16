import os

# AUTH
import pyrebase

# DB
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def initialize_firebase():
    config = {
        "apiKey": os.getenv("API_KEY"),
        "authDomain": os.getenv("AUTH_DOMAIN"),
        "databaseURL": os.getenv("DB_URL"),
        "storageBucket": os.getenv("STORAGE_BUCKET"),
        "serviceAccount": os.getenv("SERVICE_ACCOUNT")
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    cred = credentials.Certificate(os.getenv("SERVICE_ACCOUNT"))
    firebase_admin.initialize_app(cred)
    firestore_db = firestore.client()
    return auth, firestore_db


auth, firestore_db = initialize_firebase()
