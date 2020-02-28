import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('.\confidential.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

data = {"userId":"SHC4ryzoTNMzh58qMp79sM6Cbvp1",
"foodPreferences":[{"html":"AMERICAN","id":0,"clicked":False,"style":{"background-image":"url(/dist/americanfood.jpg?7f33bb876e75866f94f6e72a063c47fd)","background-size":"cover"}}
,{"html":"INDIAN","id":1,"clicked":True,"style":{"background-image":"url(/dist/indianfood.jpg?917aa4d24c4f4e210a627bcfa0d782ee)","background-size":"cover"}},{"html":"ITALIAN",
"id":2,"clicked":False,"style":{"background-image":"url(/dist/italianfood4.jpg?cb07f8026c785009b96cf56325f219ee)","background-size":"cover"}}
,{"html":"JAPANESE","id":3,"clicked":True,"style":{"background-image":"url(/dist/japanesefood5.jpg?c102f210b0879e33f809b2c33386492d)","background-size":"cover"}}],"activityPreferences":[{"html":"TOURISM","id":0,"clicked":True,"style":{"background-image":"url(/dist/tourism.jpg?233f37a417ebc63b5e88df47eebb9e96)","background-size":"cover"}},{"html":"slide2","id":1,"clicked":False,"style":{"background":"#4bbfc3"}},{"html":"slide3","id":2,"clicked":True,"style":{"background":"#7baabe"}},{"html":"slide4","id":3,"clicked":False,"style":{"background":"#7baabe"}}]}


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
  snapshot.update({"selectedPreferences": "true"})
  return "ok"

print(assignPreferences(data))
