import json
from fastapi import APIRouter, Request, Body
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from .models import Interest, UpdateInterest
from typing import List
from bson import json_util, ObjectId

router = APIRouter(prefix='/interests')

# ================== START /interests endpoint ==================


# GET all interests
@router.get('', response_model=List[Interest])
def get_all_interests(request: Request):
    interests = list(request.app.db['interests'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(interests, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, "No interests found!")


# CREATE a new interest
@router.post('', response_model=Interest)
def create_a_new_interest(request: Request, interest: Interest = Body(...)):
    newinterest = interest.dict()
    request.app.db['interests'].insert_one(newinterest)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newinterest, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 201)

    raise HTTPException(400, "Bad request")


# GET an interest by id
@router.get('/{id}', response_model=Interest)
def get_an_interest_by_id(id: str, request: Request):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['interests'].count_documents({"_id": ObjectId(id)}) == 0:
        raise HTTPException(404, f"Interest with id {id} does not exist!")

    interest = request.app.db['interests'].find_one({"_id": ObjectId(id)})
    response = json.loads(json.dumps(interest, default=json_util.default))

    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, f"interest with id {id} not found")


# UPDATE an interest by id
@router.put('/{id}', response_model=UpdateInterest)
def update_an_interest_by_id(id: str, request: Request, interest: UpdateInterest = Body(...)):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['interests'].count_documents({"_id": ObjectId(id)}) == 0:
        raise HTTPException(404, f"Interest with id {id} does not exist!")

    updatedInterest = interest.dict()
    request.app.db['interests'].update_one({"_id": ObjectId(id)}, {"$set": updatedInterest})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedInterest, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, f"interest with id {id} does not exist!")


# DELETE an interest by id
@router.delete('/{id}', response_model=Interest)
def delete_an_interest_by_id(id: str, request: Request):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['interests'].count_documents({"_id": ObjectId(id)}) == 0:
        raise HTTPException(404, f"Interest with id {id} does not exist!")

    deletedInterest = request.app.db["interests"].delete_one({"_id": ObjectId(id)})

    if deletedInterest.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted interest with id {id}")

    raise HTTPException(status_code=404, detail=f"interest with id {id} not found")
# ================== END /interests endpoint ==================
