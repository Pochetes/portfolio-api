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
def getInterests(request: Request):
    interests = list(request.app.db['interests'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(interests, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
       raise HTTPException(400, "No interests found!")

# CREATE a new interest
@router.post('', response_model=Interest)
def createInterest(request: Request, interest: Interest = Body(...)):
    newinterest = interest.dict()
    request.app.db['interests'].insert_one(newinterest)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newinterest, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Bad request")

# GET an interest by id
@router.get('/{id}', response_model=Interest)
def getInterest(id: str, request: Request):
    interest = request.app.db['interests'].find_one({"_id": ObjectId(id)})
    response = json.loads(json.dumps(interest, default=json_util.default))
    
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(404, f"interest with id {id} not found")

# UPDATE an interest by id
@router.put('/{id}', response_model=UpdateInterest)
def updateInterest(id: str, request: Request, interest: UpdateInterest = Body(...)):
    updatedInterest = interest.dict()
    request.app.db['interests'].update_one({"_id": ObjectId(id)}, { "$set": updatedInterest})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedInterest, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, f"interest with id {id} does not exist!")

# DELETE an interest by id
@router.delete('/{id}', response_model=Interest)
def deleteInterest(id: str, request: Request):
    deletedInterest = request.app.db["interests"].delete_one({"_id": ObjectId(id)})

    if deletedInterest.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted interest with id {id}")

    raise HTTPException(status_code=404, detail=f"interest with id {id} not found")
# ================== END /interests endpoint ==================