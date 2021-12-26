import json

from bson import json_util
from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse

from ..auth import has_access
from .models import UpdateUser, User

router = APIRouter(prefix='/user')

# references mongoDB instantiation across entire FastAPI app
# Request.app.db['user']

# ================== START /user endpoint ==================


# GET all users (should only be me)
@router.get('', response_model=User)
def get_all_users(request: Request):
    foundUser = list(request.app.db['user'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(foundUser, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, "user does not exist!")


# CREATE a new user (should only be done once)
@router.post('', response_model=User, dependencies=[Depends(has_access)])
def create_a_new_user(user: User, request: Request):  # CAN ONLY BE DONE ONCE
    newUser = user.dict()
    request.app.db['user'].insert_one(newUser)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newUser, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 201)
    raise HTTPException(400, "Bad Request")


# UPDATE the current user (should only be description)
@router.put('', response_model=UpdateUser, dependencies=[Depends(has_access)])
def update_the_current_user(firstName: str, user: User, request: Request):
    if request.app.db['user'].count_documents({"firstName": firstName}) == 0:
        raise HTTPException(404, f"User with first name {firstName} does not exist!")

    updatedUser = user.dict()
    request.app.db['user'].update_one({"firstName": firstName}, {"$set": updatedUser})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedUser, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, "user does not exist!")
# ================== END /user endpoint ==================
