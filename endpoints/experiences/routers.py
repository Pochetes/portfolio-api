import json
from typing import List

from bson import ObjectId, json_util
from fastapi import APIRouter, Body, Depends, Request
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse

from ..auth import has_access
from .models import Experience, UpdateExperience

router = APIRouter(prefix='/experiences')

# ================== START /experiences endpoint ==================


# GET all experiences
@router.get('', response_model=List[Experience])
def get_all_experiences(request: Request):
    experiences = list(request.app.db['experiences'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(experiences, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, "No experiences found!")


# CREATE a new experience
@router.post('', response_model=Experience, dependencies=[Depends(has_access)])
def create_a_new_experience(request: Request, experience: Experience = Body(...)):
    newExperience = experience.dict()
    request.app.db['experiences'].insert_one(newExperience)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newExperience, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 201)

    raise HTTPException(400, "Bad request")


# GET an experience by id
@router.get('/{id}', response_model=Experience)
def get_an_experience_by_id(id: str, request: Request):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['experiences'].count_documents({"_id": ObjectId(id)}) == 0:
        raise HTTPException(404, f"Experience with id {id} does not exist!")

    experience = request.app.db['experiences'].find_one({"_id": ObjectId(id)})

    response = json.loads(json.dumps(experience, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, f"Experience with id {id} not found")


# UPDATE an experience by id
@router.put('/{id}', response_model=UpdateExperience, dependencies=[Depends(has_access)])
def update_an_experience_by_id(id: str, request: Request, experience: UpdateExperience = Body(...)):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['experiences'].count_documents({"_id": ObjectId(id)}) == 0:
        raise HTTPException(404, f"Experience with id {id} does not exist!")

    updatedExperience = experience.dict()
    request.app.db['experiences'].update_one({"_id": ObjectId(id)}, {"$set": updatedExperience})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedExperience, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, f"Experience with id {id} does not exist!")


# DELETE an experience by id
@router.delete('/{id}', response_model=Experience, dependencies=[Depends(has_access)])
def delete_an_experience_by_id(id: str, request: Request):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['experiences'].count_documents({"_id": ObjectId(id)}) == 0:
        raise HTTPException(404, f"Experience with id {id} does not exist!")

    deletedExperience = request.app.db["experiences"].delete_one({"_id": ObjectId(id)})

    if deletedExperience.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted experience with id {id}")

    raise HTTPException(status_code=404, detail=f"Experience with id {id} not found")
# ================== END /experiences endpoint ==================
