import json
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from ..models import User, UpdateUser
from database import db
from bson import json_util

userRouter = APIRouter(prefix='/user',)
userCollection = db['user']

@userRouter.get('/', response_model=User)
def getUser():
    foundUser = list(userCollection.find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(foundUser, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        HTTPException(400, "Person does not exist!")

@userRouter.post('/', response_model=User)
def createPerson(user: User): # CAN ONLY BE DONE ONCE
    newUser = user
    userCollection.insert_one(newUser)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newUser, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        HTTPException(400, "Bad Request")
    

@userRouter.put('/', response_model=UpdateUser)
def updatePerson(firstName: str, user: User):
    updatedUser = user
    userCollection.update_one({"firstName": firstName}, { "$set": updatedUser})
    userCollection.find_one({"firstName": firstName})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedUser, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        HTTPException(400, "Person does not exist!")
