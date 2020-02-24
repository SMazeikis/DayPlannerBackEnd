import pyrebase

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

firebase = pyrebase.initialize_app(config)


# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
#user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])
def fer():
    try:
        return("hello")
    except:
        return("what")