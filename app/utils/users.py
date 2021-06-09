from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def get_users():
    query = f"""
    SELECT * 
    FROM prueba
    """
    db.connect()
    result = db.select_rows(query)
    return result
