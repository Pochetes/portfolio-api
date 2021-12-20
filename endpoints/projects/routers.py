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
def getProjects(request: Request):
    projects = list(request.app.db['projects'].find({}))
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(projects, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
       raise HTTPException(400, "No projects found!")

# CREATE a new project
@router.post('', response_model=Project)
def createProject(request: Request, project: Project = Body(...)):
    newProject = project.dict()
    request.app.db['projects'].insert_one(newProject)
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(newProject, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Bad request")

# GET an project by id
@router.get('/{id}', response_model=Project)
def getProject(id: str, request: Request):
    project = request.app.db['projects'].find_one({"_id": ObjectId(id)})
    response = json.loads(json.dumps(project, default=json_util.default))
    
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(404, f"project with id {id} not found")

# UPDATE an project by id
@router.put('/{id}', response_model=UpdateProject)
def updateProject(id: str, request: Request, project: UpdateProject = Body(...)):
    updatedProject = project.dict()
    request.app.db['projects'].update_one({"_id": ObjectId(id)}, { "$set": updatedProject})
    # converts list object to str (JSON format)
    # converts str obj to JSON type (avoids escape double quotes)
    response = json.loads(json.dumps(updatedProject, default=json_util.default))
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, f"project with id {id} does not exist!")

# DELETE an project by id
@router.delete('/{id}', response_model=Project)
def deleteProject(id: str, request: Request):
    deletedProject = request.app.db["projects"].delete_one({"_id": ObjectId(id)})

    if deletedProject.deleted_count == 1:
        return JSONResponse(status_code=204, content=f"Deleted project with id {id}")

    raise HTTPException(status_code=404, detail=f"project with id {id} not found")
# ================== END /projects endpoint ==================