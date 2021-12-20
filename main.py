import os, uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
from functools import lru_cache
from config import settings

from endpoints.user.routers import router as userRouter
from endpoints.contacts.routers import router as contactsRouter
from endpoints.skills.routers import router as skillsRouter
from endpoints.experiences.routers import router as experiencesRouter
from endpoints.interests.routers import router as interestsRouter
from endpoints.projects.routers import router as projectsRouter

load_dotenv()
MONGODB_URI = os.environ[settings.DB_URL]

@lru_cache
def getSettings():
    return settings

getSettings()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESC,
    version=settings.VERSION,
    contact=settings.CONTACT,
    license_info=settings.LICENSE
)

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

@app.on_event("startup")
def startupDBClient():
    app.client = MongoClient(MONGODB_URI)
    app.db = app.client[settings.DB_NAME]

@app.on_event("shutdown")
def shutdownDBClient():
    app.client.close()

app.include_router(userRouter, tags=["user"])
app.include_router(contactsRouter, tags=["contacts"])
app.include_router(skillsRouter, tags=['skills'])
app.include_router(experiencesRouter, tags=['experiences'])
app.include_router(interestsRouter, tags=['interests'])
app.include_router(projectsRouter, tags=['projects'])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.DEBUG_MODE,
    )