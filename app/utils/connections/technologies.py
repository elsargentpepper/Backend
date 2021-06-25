from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def get_technology_id(technology):

    query = f"""
    SELECT technologies_id 
    FROM technologies 
    WHERE name = '{technology}' 
    """

    db.connect()
    result = db.select_rows(query)
    return result


def get_technology_name(technology_id):

    query = f"""
    SELECT name
    FROM technologies 
    WHERE technologies_id = '{technology_id}' limit 1
    """

    db.connect()
    result = db.select_rows(query)
    return result[0][0]


def get_all_technologies():
    query = f"""
    SELECT * 
    FROM technologies
    """

    db.connect()
    result = db.select_rows(query)
    return result