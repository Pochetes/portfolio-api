from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from models import InfoModel, UpdateInfoModel

from database import (
    getPerson,
    createPerson,
    updatePerson
)

app = FastAPI()

# ========= CORS Middleware =========
origins = [
    "http://pochetes.herokuapp.com/personal",
    "http://pochetes.herokuapp.com/experiences",
    "http://pochetes.herokuapp.com/projects",
    "https://pochetes.herokuapp.com/personal",
    "https://pochetes.herokuapp.com/experiences",
    "https://pochetes.herokuapp.com/projects",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8000/personal",
    "http://localhost:8000/experiences",
    "http://localhost:8000/projects",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========= ENDPOINTS =========
@app.get(
    '/personal/info', 
    response_description="Retrieves the main details about me: full name, email and description.",
    response_model=InfoModel
)
def get_person():
    response = getPerson()
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Person does not exist!")    

@app.post(
    '/personal/info', 
    response_description="Create a new person (once).", 
    response_model=InfoModel
)
def create_person(info: InfoModel = Body(...)):
    response = createPerson(info.dict())
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Bad Request")

@app.put(
    '/personal/info',
    response_description="Updates the main details about me (should only be the description).",
    response_model=InfoModel
)
def update_person(firstName: str, info: UpdateInfoModel = Body(...)):
    response = updatePerson(firstName, info.dict())
    if response:
        return JSONResponse(response, 200)
    else:
        raise HTTPException(400, "Person does not exist!")