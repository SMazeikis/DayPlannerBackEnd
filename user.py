import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./confidential.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


def assignPreferences(data):
  userId = data["userId"]
  snapshot = db.collection('users').document(userId)
  foodDict = {}
  activityDict = {}
  for choice in data["foodPreferences"]:
    if choice["clicked"]:
        foodDict[choice["html"]] = True
    else:
        pass
  for choice in data["activityPreferences"]:
    if choice["clicked"]:
        activityDict[choice["html"]] = True
    else:
        pass
  snapshot.set(foodDict,merge=True)
  snapshot.set(activityDict, merge=True)
  return "ok"

