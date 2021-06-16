from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.post("/users/create")
async def POST_users(   
    name: str,
    email: str,
    password: str,  
    login_type: str,
):
    hashed = bcrypt.hashpw(bytes(password, encoding='utf-8'),bcrypt.gensalt())
    messege = add_user(name,email,hashed.decode("utf-8"),login_type)

    return {"response": messege}
