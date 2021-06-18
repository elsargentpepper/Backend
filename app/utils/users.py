from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def add_user(name,email,password,login_type,username):
    query = f"""
        insert into users(name,email,password,login_type,username) values (%s, %s, %s, %s,%s)
    """
    db.connect()
    result = db.insert_row(query,(name,email,password,login_type,username))

    return result
    

def get_user(username):
    query = f"""
    SELECT * 
    FROM users 
    WHERE username = '{username}' 
    """
    db.connect()
    result = db.select_rows(query)
    return result

def get_all_users():
    query = f"""
    SELECT * 
    FROM users
    """
    db.connect()
    result = db.select_rows(query)
    return result

def get_questions(technology,level):

    query = f"""
    SELECT q.question,q.answers,q.image
    FROM questions as q
    INNER JOIN  technologies as t
    ON q.technology = t.technologies_id
    INNER JOIN levels as l
    on q.level = l.levels_id
    WHERE t.name = '{technology}' AND l.name = '{level}'
    """
    db.connect()
    result = db.select_rows(query)


    return result