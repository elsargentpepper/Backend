from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def add_user(name,email,password,login_type,username):

    query = f"""
    INSERT INTO users(name,email,password,login_type,username,badges,prefered_technologies)
    VALUES (%s, %s, %s, %s,%s,%s,%s)
    """

    db.connect()
    result = db.insert_row(query,(name,email,password,login_type,username,[],[]))

    return result


def get_user_by_username(username):

    query = f"""
    SELECT * 
    FROM users 
    WHERE username = '{username}' 
    """

    db.connect()
    result = db.select_rows(query)
    return result


def get_user_by_email(email):

    query = f"""
    SELECT * 
    FROM users 
    WHERE email = '{email}' 
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


def update_user(user):

    query = f"""
    UPDATE users
    SET name = %s,
        password = %s,
        login_type = %s,
        username = %s,
        badges = %s,
        prefered_technologies = %s,
        profile_pic = %s,
        email = %s
    WHERE users_id = %s
    """

    db.connect()
    result = db.update_row(query,(user["name"],
                                user["password"],
                                user["login_type"],
                                user["username"],
                                user["badges"],
                                user["prefered_technologies"],
                                user["profile_pic"],
                                user["email"],
                                user["id"]
                                ))

    return result


def delete_user(user):

    query = f"""
    DELETE
    FROM users
    WHERE email = %s AND username = %s
    """

    db.connect()
    result = db.delete_row(query,(user["email"],user["username"]))

    return result