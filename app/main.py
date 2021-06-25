from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

from typing import List, Optional
from pydantic import BaseModel
import bcrypt

from app.core.config import settings

import app.utils.connections.users as User_conn
import app.utils.connections.levels as Level_conn
import app.utils.connections.progress as Progresses_conn
import app.utils.connections.questions as Questions_conn
import app.utils.connections.technologies as Tech_conn

from app.utils.questions_formating import questions_formating,check_question
from app.utils.users_formating import user_format,users_format,user_format_body
from app.utils.progress_formating import progresses_format,progress_percentage_formating
from app.utils.badge_identification import badge_identification
from app.utils.question_validation import question_validation
from app.utils.technologies_formating import technologies_formating
from app.utils.levels_formating import levels_formating

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
    name: Optional[str]
    email: Optional[str]
    password: Optional[str] = None
    login_type: Optional[str]
    username: Optional[str]
    badges: Optional[List] = None
    prefered_technologies: Optional[List] = None
    profile_pic: Optional[str] = ""

class Technology(BaseModel):
    name: str

class Progress(BaseModel):
    percentage: int
    user: Users
    technology: Technology

class Questions(BaseModel):
    answers: List[str]
    image: str
    level: int
    technology: int
    question: str
    right_answer: str
    password: str



@app.post("/users/create")
async def post_users(user: Users):

    hashed = bcrypt.hashpw(bytes(user.password, encoding='utf-8'),bcrypt.gensalt()) # THIS NEEDS TO BE A FUNCTION SOMEWHERE ELSE

    User_conn.add_user(user.name,user.email,hashed.decode("utf-8"),user.login_type,user.username)

    return {"response": "User created"}



@app.get("/user")
async def get_user( username: str=None,
                    email: str=None
 ):

    if username != None and email == None:
        user = User_conn.get_user_by_username(username)

    elif email != None and username == None:
        user = User_conn.get_user_by_email(email)
        
    else:
        raise HTTPException(status_code=400, detail="Please only send either email or username")

    if len(user) < 1:
        raise HTTPException(status_code=400, detail="Sorry this user does not exist")
    
    response = user_format(user[0])

    return {"response": response}



@app.get("/users")
async def get_users():

    users = User_conn.get_all_users()
    response = users_format(users)
    return {"response": response}



@app.put("/user/edit")
async def update_user(user: Users):

    info = User_conn.get_user_by_username(user.username)

    if info[0] == None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    original_user = user_format(info[0])

    user_updated = dict()
    user_updated["id"] = original_user["id"]
    user_updated["name"] = user.name or original_user["name"]
    user_updated["password"] = user.password or original_user["password"]
    user_updated["login_type"] = user.login_type or original_user["login_type"]
    user_updated["username"] = user.username or original_user["username"]
    user_updated["email"] = user.email or original_user["email"]
    user_updated["badges"] = user.badges or original_user["badges"]
    user_updated["prefered_technologies"] = user.prefered_technologies or original_user["prefered_technologies"]
    user_updated["profile_pic"] = user.profile_pic or original_user["profile_pic"]
    User_conn.update_user(user_updated)

    return {"response": "User updated"}



@app.delete("/user/delete")
async def delete_user(user: Users):

    info = User_conn.get_user_by_username(user.username)

    if info[0] == None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    original_user = user_format(info[0])

    User_conn.delete_user(original_user)

    return {"response": "User delete"}



@app.get("/questions")
async def get_questions(
    technology: str,
    level: str,
    number_of_questions: int = 5,
):

    questions = Questions_conn.get_questions(technology,level)

    if len(questions) < number_of_questions:
        raise HTTPException(status_code=400, detail="Sorry we don't have that many questions of this specific type")  

    response = questions_formating(questions,number_of_questions)
    response = check_question(response)
    return {"response": response}



@app.post("/user/technology/add")
async def post_user_technology_add(
    user: Users,
    technology: Technology
    ):

    users = User_conn.get_user_by_username(user.username)

    if users[0] == None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    user_to_update = user_format(users[0])

    if user_to_update["prefered_technologies"] != None and technology.name in user_to_update["prefered_technologies"]: 
        raise HTTPException(status_code=400, detail="Sorry you can not add the same to technology twice")

    user_to_update["prefered_technologies"].append(technology.name)

    user_updated = dict()
    user_updated["id"] = user_to_update["id"]
    user_updated["name"] = user.name or user_to_update["name"]
    user_updated["password"] = user.password or user_to_update["password"]
    user_updated["login_type"] = user.login_type or user_to_update["login_type"]
    user_updated["username"] = user.username or user_to_update["username"]
    user_updated["email"] = user.email or user_to_update["email"]
    user_updated["badges"] = user.badges or user_to_update["badges"]
    user_updated["prefered_technologies"] = user.prefered_technologies or user_to_update["prefered_technologies"]
    user_updated["profile_pic"] = user.profile_pic or user_to_update["profile_pic"]

    User_conn.update_user(user_updated)

    Progresses_conn.add_user_progress(technology.name,user_to_update['id'])
    
    return {"response": user_updated}



@app.delete("/user/technology/remove")
async def delete_user_technology_remove(
    user: Users,
    technology: Technology
    ):

    users = User_conn.get_user_by_username(user.username)

    if users[0] == None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    user_to_update = user_format(users[0])

    if not technology.name in user_to_update["prefered_technologies"]:
        raise HTTPException(status_code=400, detail="Sorry you do not have that technology in the first place")

    user_to_update["prefered_technologies"].remove(technology.name)

    user_updated = dict()
    user_updated["id"] = user_to_update["id"]
    user_updated["name"] = user.name or user_to_update["name"]
    user_updated["password"] = user.password or user_to_update["password"]
    user_updated["login_type"] = user.login_type or user_to_update["login_type"]
    user_updated["username"] = user.username or user_to_update["username"]
    user_updated["email"] = user.email or user_to_update["email"]
    user_updated["badges"] = user.badges or user_to_update["badges"]
    user_updated["prefered_technologies"] = user.prefered_technologies or user_to_update["prefered_technologies"]
    user_updated["profile_pic"] = user.profile_pic or user_to_update["profile_pic"]

    User_conn.update_user(user_updated)
    
    Progresses_conn.remove_user_progress(technology.name,user_to_update['id'])

    return {"response": user_updated}



@app.put("/user/progress/update")
async def update_user_update_progress(
    progress: Progress
    ):
    
    user_info = User_conn.get_user_by_username(progress.user.username)


    if len(user_info) < 1:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    user = user_format(user_info[0])
    user_id = user["id"]
 
    percentage = Progresses_conn.get_user_progress_by_tech(user_id,progress.technology.name)

    if percentage >= progress.percentage:
        return {"response": user}
    else:

        Progresses_conn.update_user_progress(progress.percentage,user_id,progress.technology.name)

        progress_info = Progresses_conn.get_user_progress(user_id)

        progresses = progresses_format(progress_info)

        user_updated = badge_identification(progresses["users_progresses"],user)

        User_conn.update_user(user_updated)

    return {"response": user_updated}



@app.post("/questions/add")
async def post_questions(question: Questions):

    if question.password != settings.QUESTIONS_PASSWORD:
        raise HTTPException(status_code=401, detail="Authorization denied")


    valid = question_validation(question)
    if valid:
        raise HTTPException(status_code=400, detail="This question all ready exist in out data base")

    
    Questions_conn.add_questions(question)
    
    return {"response": question}



@app.get("/user/progress")
async def get_user_progress( username: str ):

    user = User_conn.get_user_by_username(username)

    if len(user) < 1:
        raise HTTPException(status_code=400, detail="Sorry this user does not exist")
    
    user_formated = user_format(user[0])

    progresses = Progresses_conn.get_progress(user_formated)

    if len(progresses) < 1:
        raise HTTPException(status_code=400, detail="Sorry this user does not have any progress")

    response = progress_percentage_formating(progresses)
    
    return response



@app.get("/technologies")
async def get_technologies():

    info = Tech_conn.get_all_technologies()

    response = technologies_formating(info)    

    
    return response



@app.get("/levels")
async def get_levels():

    info = Level_conn.get_all_levels()

    response = levels_formating(info)    

    
    return response    