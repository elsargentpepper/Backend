from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def get_all_levels():
    query = f"""
    SELECT name 
    FROM levels
    """

    db.connect()
    result = db.select_rows(query)
    return result