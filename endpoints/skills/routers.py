import json
from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from .models import Skill, UpdateSkill
from typing import List
from bson import json_util


router = APIRouter(prefix='/skills')

# ================== START /skills endpoint ==================

# GET all skills (i.e Python, C, JavaScript)
@router.get('/', response_model=List[Skill])
def getSkills(request: Request):
    skills = list(request.app.db['skills'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(skills, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
       raise HTTPException(400, "No skills found!")

# CREATE a new skill
@router.post('/', response_model=Skill)
def createSkill(skill: Skill, request: Request):
    newSkill = skill.dict()
    request.app.db['skills'].insert_one(newSkill)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newSkill, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Bad request")

# GET a skill by skill type
@router.get('/{technology}', response_model=Skill)
def getSkill(technology: str, request: Request):
    oneSkill = request.app.db['skills'].find_one({"technology": technology})

    response = json.loads(json.dumps(oneSkill, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(404, f"{technology} skill not found")

# UPDATE a contact by title
@router.put('/{technology}', response_model=UpdateSkill)
def updateSkill(technology: str, skill: Skill, request: Request):
    updatedSkill = skill.dict()
    request.app.db['skills'].update_one({"technology": technology}, { "$set": updatedSkill})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedSkill, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Person does not exist!")

# DELETE a skill by skill type
@router.delete('/{technology}', response_model=Skill)
def deleteSkill(technology: str, request: Request):
    deletedSkill = request.app.db["skills"].delete_one({"technology": technology})

    if deletedSkill.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted {technology} skill")

    raise HTTPException(status_code=404, detail=f"{technology} skill not found")

# ================== END /skills endpoint ==================
