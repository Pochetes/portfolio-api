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
@router.get('', response_model=List[Skill])
def get_all_skills(request: Request):
    skills = list(request.app.db['skills'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(skills, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(400, "No skills found!")

# CREATE a new skill
@router.post('', response_model=Skill)
def create_a_new_skill(skill: Skill, request: Request):
    newSkill = skill.dict()
    request.app.db['skills'].insert_one(newSkill)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newSkill, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, "Bad request")

# GET a skill by skill type
@router.get('/{technology}', response_model=Skill)
def get_a_skill_by_technology(technology: str, request: Request):
    # check if technology exists in MongoDB db
    if request.app.db['skills'].find({"technology": technology}, {"$exists": False}):
        raise HTTPException(400, f"{technology} skill does not exist!")

    oneSkill = request.app.db['skills'].find_one({"technology": technology})

    response = json.loads(json.dumps(oneSkill, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, f"{technology} skill not found")

# UPDATE a skill by skill type
@router.put('/{technology}', response_model=UpdateSkill)
def update_a_skill_by_technology(technology: str, skill: Skill, request: Request):
    # check if technology exists in MongoDB db
    if request.app.db['skills'].find({"technology": technology}, {"$exists": False}):
        raise HTTPException(400, f"{technology} skill does not exist!")

    updatedSkill = skill.dict()
    request.app.db['skills'].update_one({"technology": technology}, { "$set": updatedSkill})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedSkill, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(400, "Person does not exist!")

# DELETE a skill by skill type
@router.delete('/{technology}', response_model=Skill)
def delete_a_skill_by_technology(technology: str, request: Request):
    # check if technology exists in MongoDB db
    if request.app.db['skills'].find({"technology": technology}, {"$exists": False}):
        raise HTTPException(400, f"{technology} skill does not exist!")

    deletedSkill = request.app.db["skills"].delete_one({"technology": technology})

    if deletedSkill.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted {technology} skill")

    raise HTTPException(status_code=404, detail=f"{technology} skill not found")

# ================== END /skills endpoint ==================
