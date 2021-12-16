import os
import json
from models import InfoModel
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import json_util

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

db = client['portfolio']
personCol = db.person


# GET
def getPerson():
    person = list(personCol.find({}))
    return json.dumps(person, default=json_util.default)

# POST
def createPerson(info: InfoModel): # CAN ONLY BE DONE ONCE
    person = info
    personCol.insert_one(person)
    return json.dumps(person, default=json_util.default)

# PUT
def updatePerson(firstName: str, info: InfoModel):
    person = info
    personCol.update_one({"firstName": firstName}, { "$set": person})
    personCol.find_one({"firstName": firstName})
    return json.dumps(person, default=json_util.default)