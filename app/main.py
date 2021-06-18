from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import bcrypt

from app.core.config import settings
from app.utils.users import get_user, add_user

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

if settings.ENVIRONMENT == "production":
    origins = [settings.CLIENT]
else:
    origins = [
        "http://localhost:3000",
        "http://localhost:8080",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
        name: str
        email: str
        password: str
        login_type: str
        username: str


@app.post("/users/create")
async def POST_users(user: User):
    hashed = bcrypt.hashpw(bytes(user.password, encoding='utf-8'),bcrypt.gensalt()) # THIS NEEDS TO BE A FUNCTION SOMEWHERE ELSE
    messege = add_user(user.name,user.email,hashed.decode("utf-8"),user.login_type,user.username)

    return {"response": messege}


@app.get("/user")
async def GET_users(   
    username: str ,
):
    

    return {"response": "messege"}