from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def add_user(name,email,password,login_type):
    query = f"""
        insert into users(name,email,password,login_type) values (%s, %s, %s, %s)
    """
    db.connect()
    result = db.insert_row(query,(name,email,password,login_type))

    return result
    

def get_user():
    query = f"""
    SELECT * 
    FROM prueba
    """
    db.connect()
    result = db.select_rows(query)
    return result