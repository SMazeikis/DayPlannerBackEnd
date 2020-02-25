import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./confidential.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

snapshot = db.collection('users').document("NUB1BGl5H0gqDi2JPYRzflO6GEF3")

def test():
  return "test success :D"