import json
from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from .models import User, UpdateUser
from bson import json_util

router = APIRouter(prefix='/user')

# references mongoDB instantiation across entire FastAPI app
# Request.app.db['user']

# ================== START /user endpoint ==================

# GET all users (should only be me)
@router.get('', response_model=User)
def getUser(request: Request):
    foundUser = list(request.app.db['user'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(foundUser, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Person does not exist!")

# CREATE a new user (should only be done once)
@router.post('', response_model=User)
def createPerson(user: User, request: Request): # CAN ONLY BE DONE ONCE
    newUser = user.dict()
    request.app.db['user'].insert_one(newUser)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newUser, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Bad Request")
    
# UPDATE the current user (should only be description)
@router.put('', response_model=UpdateUser)
def updatePerson(firstName: str, user: User, request: Request):
    updatedUser = user.dict()
    request.app.db['user'].update_one({"firstName": firstName}, { "$set": updatedUser})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedUser, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Person does not exist!")
# ================== END /user endpoint ==================