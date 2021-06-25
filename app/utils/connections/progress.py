from app.db.connection import Database
from app.core.config import settings

db = Database(settings)

from app.utils.connections.technologies import get_technology_id 

def add_user_progress(technology,user_id):

    tech = get_technology_id(technology)
    tech_id = tech[0]

    query = f"""
    INSERT INTO progress(percentage,user_id,technology)
    VALUES (%s, %s, %s)
    """

    db.connect()
    result = db.insert_row(query,(0,user_id,tech_id))

    return result


def remove_user_progress(technology,user_id):

    tech = get_technology_id(technology)
    tech_id = tech[0]

    query = f"""
    DELETE
    FROM progress
    WHERE technology = %s AND user_id = %s
    """

    db.connect()
    result = db.insert_row(query,(tech_id,user_id))

    return result 


def update_user_progress(percentage,user_id,technology):

    tech = get_technology_id(technology)
    tech_id = tech[0]

    query = f"""
    UPDATE progress
    SET percentage = %s
    WHERE user_id = %s AND technology = %s
    """

    db.connect()
    result = db.update_row(query,(percentage,user_id,tech_id))

    return result


def get_user_progress_by_tech(user_id,technology):

    tech = get_technology_id(technology)
    tech_id = tech[0]

    query = f"""
    SELECT percentage
    FROM progress
    WHERE user_id = {user_id} AND technology ={tech_id[0]}
    """

    db.connect()
    result = db.select_rows(query)

    return result[0][0]


def get_user_progress(user_id):


    query = f"""
    SELECT *
    FROM progress
    WHERE user_id = {user_id}
    """

    db.connect()
    result = db.select_rows(query)

    return result


def get_progress(user):

    query = f"""
    SELECT p.percentage, t.name 
    FROM progress as p 
    JOIN technologies as t
    ON p.technology = t.technologies_id
    WHERE p.user_id = {user['id']} 
    """

    db.connect()
    result = db.select_rows(query)
    return result