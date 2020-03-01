import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('./confidential.json')
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

def assignPreferences(data):
  userId = data["userId"]
  snapshot = db.collection('users').document(userId)
  foodDict = []
  activityDict = []
  for choice in data["foodPreferences"]:
    if choice["clicked"]:
        foodDict.append(choice["html"])
    else:
        pass
  for choice in data["activityPreferences"]:
    if choice["clicked"]:
        activityDict.append(choice["html"])
    else:
        pass
  snapshot.set({"food":foodDict}, merge= True)
  snapshot.set({"activities" :activityDict}, merge=True)
  snapshot.set({"selectedPreferences": "true"}, merge=True)
  return "ok"
