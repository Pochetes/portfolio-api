from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user

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

app.include_router(user.userRouter)
