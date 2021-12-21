import json
from fastapi import APIRouter, Request, Body
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from .models import Project, UpdateProject
from typing import List
from bson import json_util, ObjectId

router = APIRouter(prefix='/projects')

# ================== START /projects endpoint ==================

# GET all projects
@router.get('', response_model=List[Project])
def get_all_projects(request: Request):
    projects = list(request.app.db['projects'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(projects, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(400, "No projects found!")

# CREATE a new project
@router.post('', response_model=Project)
def create_a_new_project(request: Request, project: Project = Body(...)):
    newProject = project.dict()
    request.app.db['projects'].insert_one(newProject)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newProject, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, "Bad request")

# GET a project by id
@router.get('/{id}', response_model=Project)
def get_a_project_by_id(id: str, request: Request):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['projects'].find({"_id": ObjectId(id)}, {"$exists": False}):
        raise HTTPException(400, f"Project with id {id} does not exist!")    
    
    project = request.app.db['projects'].find_one({"_id": ObjectId(id)})
    response = json.loads(json.dumps(project, default=json_util.default))
    
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(404, f"project with id {id} not found")

# UPDATE a project by id
@router.put('/{id}', response_model=UpdateProject)
def update_a_project_by_id(id: str, request: Request, project: UpdateProject = Body(...)):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['projects'].find({"_id": ObjectId(id)}, {"$exists": False}):
        raise HTTPException(400, f"Project with id {id} does not exist!")    
    
    updatedProject = project.dict()
    request.app.db['projects'].update_one({"_id": ObjectId(id)}, { "$set": updatedProject})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedProject, default=json_util.default))
    if response is not None:
        return JSONResponse(response, 200)

    raise HTTPException(400, f"project with id {id} does not exist!")

# DELETE a project by id
@router.delete('/{id}', response_model=Project)
def delete_a_project_by_id(id: str, request: Request):
    # check if valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(404, f"id {id} is invalid")

    # check if valid ObjectId exists!
    if request.app.db['projects'].find({"_id": ObjectId(id)}, {"$exists": False}):
        raise HTTPException(400, f"Project with id {id} does not exist!")

    deletedProject = request.app.db["projects"].delete_one({"_id": ObjectId(id)})

    if deletedProject.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted project with id {id}")

    raise HTTPException(status_code=404, detail=f"project with id {id} not found")
# ================== END /projects endpoint ==================