import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  "apiKey" : "AIzaSyDQT78_79sRW4nPY2hj_2zu6TX_V3VoD8k",
  "authDomain" : "dayplanner-740b3.firebaseapp.com",
  "databaseURL" : "https://dayplanner-740b3.firebaseio.com",
  "projectId" : "dayplanner-740b3",
  "storageBucket" : "dayplanner-740b3.appspot.com",
  "messagingSenderId" : "930720206669",
  "appId" : "1:930720206669:web:2d15a4b9f7ec24b1b7f104",
  "measurementId" : "G-QZFMJ335XN"
}

# Use a service account
cred = credentials.Certificate('dayplanner-backend/nothing.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

firebase = pyrebase.initialize_app(config)


# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
#user = auth.sign_in_with_email_and_password(email, password)


# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])
users_ref = db.collection(u'users')
docs = users_ref.stream()
print(docs)