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

@lru_cache
def getSettings():
    return settings

# naming settings for each class
db = getSettings().db
md = getSettings().md
mt = getSettings().mt

load_dotenv()
MONGODB_URI = os.environ[db.DB_URI]


app = FastAPI(
    title=mt.APP_NAME,
    description=mt.DESC,
    version=mt.VERSION,
    contact=mt.CONTACT,
    license_info=mt.LICENSE
)

# ========= CORS Middleware =========
app.add_middleware(
    CORSMiddleware,
    allow_origins=md.CORS_ORIGINS,
    allow_credentials=md.CORS_CRED,
    allow_methods=md.CORS_METHODS,
    allow_headers=md.CORS_HEADERS
)

@app.on_event("startup")
def startupDBClient():
    app.client = MongoClient(MONGODB_URI)
    app.db = app.client[db.DB_NAME]

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
        reload=mt.DEBUG_MODE
    )