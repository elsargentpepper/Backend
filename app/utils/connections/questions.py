from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def get_questions(technology,level):

    query = f"""
    SELECT q.question,q.answers,q.image,q.right_answer
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


def add_questions(question):

    query = f"""
    INSERT INTO questions(answers,image,level,technology,question,right_answer)
    VALUES (
        %s,%s,%s, %s, %s, %s
    )
    """

    db.connect()
    result = db.insert_row(query,(question.answers,
                            question.image,
                            question.level,
                            question.technology,
                            question.question,
                            question.right_answer))
    return result


def get_all_questions_tech(tech_id):

    query = f"""
    SELECT *
    FROM questions
    WHERE technology = {tech_id}
    )
    """

    db.connect()
    result = db.select_rows(query)
    return result