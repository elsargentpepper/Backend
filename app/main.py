from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from typing import List, Optional
from pydantic import BaseModel

import bcrypt

from app.core.config import settings

from app.utils.users import get_user, add_user, get_all_users, get_questions, update_user, delete_user,add_user_progress,remove_user_progress,update_user_progress,get_user_progress_by_tech,get_user_progress
from app.utils.questions_formating import questions_formating
from app.utils.users_formating import user_format,users_format
from app.utils.progress_formating import progresses_format
from app.utils.badge_identification import badge_identification

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

### THIS CLASSES NEED TO BE IN A DIFFERENT FILE MY DUDE

class Users(BaseModel):
    name: str
    email: str
    password: str
    login_type: str
    username: str
    badges: Optional[List] = None
    prefered_technologies: Optional[List] = None

class Technology(BaseModel):
    name: str

class Progress(BaseModel):
    percentage: int
    user: Users
    technology: Technology



@app.post("/users/create")
async def POST_users(user: Users):

    hashed = bcrypt.hashpw(bytes(user.password, encoding='utf-8'),bcrypt.gensalt()) # THIS NEEDS TO BE A FUNCTION SOMEWHERE ELSE

    add_user(user.name,user.email,hashed.decode("utf-8"),user.login_type,user.username)

    return {"response": "User created"}



@app.get("/user")
async def GET_user( username: str ):

    user = get_user(username)

    response = user_format(user[0])

    return {"response": response}



@app.get("/users")
async def GET_users():

    users = get_all_users()
    response = users_format(users)
    return {"response": response}



@app.put("/user/edit")
async def UPDATE_user(user: Users):

    update_user(user.name, user.password, user.login_type, user.username, user.email, user.badges, user.prefered_technologies)

    return {"response": "User updated"}



@app.delete("/user/delete")
async def DELETE_user(user: Users):

    delete_user(user.email, user.username,)

    return {"response": "User delete"}



@app.get("/questions")
async def GET_questions(
    technology: str,
    level: str,
    number_of_questions: int = 5,
):

    questions = get_questions(technology,level)

    if len(questions) < number_of_questions:
        raise HTTPException(status_code=400, detail="Sorry we don't have that many questions of this specific type")  

    response = questions_formating(questions,number_of_questions)
    return {"response": response}



@app.post("/user/technology/add")
async def POST_user_technology_add(
    user: Users,
    technology: Technology
    ):

    users = get_user(user.username)

    user_to_update = user_format(users[0])

    if technology.name in user_to_update["prefered_technologies"]:
        raise HTTPException(status_code=400, detail="Sorry you can not add the same to technology twice")

    user_to_update["prefered_technologies"].append(technology.name)

    update_user(user_to_update["name"],
                user_to_update["password"], 
                user_to_update["login_type"], 
                user_to_update["username"], 
                user_to_update["email"], 
                user_to_update["badges"], 
                user_to_update["prefered_technologies"])

    add_user_progress(technology.name,user_to_update['id'])
    
    return {"response": "Technology added"}



@app.delete("/user/technology/remove")
async def DELETE_user_technology_remove(
    user: Users,
    technology: Technology
    ):

    users = get_user(user.username)

    user_to_update = user_format(users[0])

    if not technology.name in user_to_update["prefered_technologies"]:
        raise HTTPException(status_code=400, detail="Sorry you do not have that technology in the first place")

    user_to_update["prefered_technologies"].remove(technology.name)

    update_user(user_to_update["name"],
                user_to_update["password"], 
                user_to_update["login_type"], 
                user_to_update["username"], 
                user_to_update["email"], 
                user_to_update["badges"], 
                user_to_update["prefered_technologies"])
    
    remove_user_progress(technology.name,user_to_update['id'])

    return {"response": "Technology removed"}



@app.put("/user/progress/update")
async def UPDATE_user_update_progress(
    progress: Progress
    ):
    
    user_info = get_user(progress.user.username)
    user = user_format(user_info[0])
    user_id = user["id"]

    percentage = get_user_progress_by_tech(user_id,progress.technology.name)

    if percentage >= progress.percentage:
        pass
    else:

        update_user_progress(progress.percentage,user_id,progress.technology.name)

        progress_info = get_user_progress(user_id)

        progresses = progresses_format(progress_info)

        user_updated = badge_identification(progresses["users_progresses"],user)

        update_user(user_updated["name"],
                        user_updated["password"], 
                        user_updated["login_type"], 
                        user_updated["username"], 
                        user_updated["email"], 
                        user_updated["badges"], 
                        user_updated["prefered_technologies"])

    return {"response": user_updated}
    