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
    WHERE username = {username}
    """
    db.connect()
    result = db.select_rows(query)
    return result