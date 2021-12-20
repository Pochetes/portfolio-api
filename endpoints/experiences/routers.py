import json
from fastapi import APIRouter, Request, Body
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from .models import Experience, UpdateExperience
from typing import List
from bson import json_util, ObjectId

router = APIRouter(prefix='/experiences')

# ================== START /experiences endpoint ==================

# GET all experiences
@router.get('', response_model=List[Experience])
def getExperiences(request: Request):
    experiences = list(request.app.db['experiences'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(experiences, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
       raise HTTPException(400, "No experiences found!")

# CREATE a new experience
@router.post('', response_model=Experience)
def createExperience(request: Request, experience: Experience = Body(...)):
    newExperience = experience.dict()
    request.app.db['experiences'].insert_one(newExperience)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newExperience, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Bad request")

# GET an experience by id
@router.get('/{id}', response_model=Experience)
def getExperience(id: str, request: Request):
    experience = request.app.db['experiences'].find_one({"_id": ObjectId(id)})

    response = json.loads(json.dumps(experience, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(404, f"Experience with id {id} not found")

# UPDATE an experience by id
@router.put('/{id}', response_model=UpdateExperience)
def updateExperience(id: str, request: Request, experience: UpdateExperience = Body(...)):
    updatedExperience = experience.dict()
    request.app.db['experiences'].update_one({"_id": ObjectId(id)}, { "$set": updatedExperience})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedExperience, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, f"Experience with id {id} does not exist!")

# DELETE an experience by id
@router.delete('/{id}', response_model=Experience)
def deleteExperience(id: str, request: Request):
    deletedExperience = request.app.db["experiences"].delete_one({"_id": ObjectId(id)})

    if deletedExperience.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted experience with id {id}")

    raise HTTPException(status_code=404, detail=f"Experience with id {id} not found")
# ================== END /experiences endpoint ==================