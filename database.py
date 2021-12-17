import os, json
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
    # converts list object to str (JSON format)
    personToStr = json.dumps(person, default=json_util.default)
    # converts str obj to JSON type (avoids escape double quotes)
    return json.loads(personToStr)

# POST
def createPerson(info: InfoModel): # CAN ONLY BE DONE ONCE
    person = info
    personCol.insert_one(person)
    # converts list object to str (JSON format)
    personToStr = json.dumps(person, default=json_util.default)
    # converts str obj to JSON type (avoids escape double quotes)
    return json.loads(personToStr)

# PUT
def updatePerson(firstName: str, info: InfoModel):
    person = info
    personCol.update_one({"firstName": firstName}, { "$set": person})
    personCol.find_one({"firstName": firstName})
    # converts list object to str (JSON format)
    personToStr = json.dumps(person, default=json_util.default)
    # converts str obj to JSON type (avoids escape double quotes)
    return json.loads(personToStr)