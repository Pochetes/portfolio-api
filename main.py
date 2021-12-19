import os, uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv

from endpoints.user.routers import router as userRouter
from endpoints.contacts.routers import router as contactsRouter
from endpoints.skills.routers import router as skillsRouter
from endpoints.experiences.routers import router as experiencesRouter

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

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

@app.on_event("startup")
def startupDBClient():
    app.client = MongoClient(MONGODB_URI)
    app.db = app.client['portfolio']

@app.on_event("shutdown")
def shutdownDBClient():
    app.client.close()

app.include_router(userRouter, tags=["user"])
app.include_router(contactsRouter, tags=["contacts"])
app.include_router(skillsRouter, tags=['skills'])
app.include_router(experiencesRouter, tags=['experiences'])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )

