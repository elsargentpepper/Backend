from app.db.connection import Database
from app.core.config import settings

db = Database(settings)

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



def get_all_questions_tech(tech_id):
    query = f"""
    SELECT *
    FROM questions 
    WHERE technology = {tech_id}
    """

    db.connect()
    result = db.select_rows(query)
    return result



def add_user(name,email,password,login_type,username):

    query = f"""
    INSERT INTO users(name,email,password,login_type,username,badges,prefered_technologies)
    VALUES (%s, %s, %s, %s,%s,%s,%s)
    """

    db.connect()
    result = db.insert_row(query,(name,email,password,login_type,username,[],[]))

    return result



def update_user(name,password,login_type,username,email,badges,pt):

    query = f"""
    UPDATE users
    SET name = %s,
        password = %s,
        login_type = %s,
        username = %s,
        badges = %s,
        prefered_technologies = %s
        
    WHERE email = %s
    """

    db.connect()
    result = db.update_row(query,(name,password,login_type,username,badges,pt,email))

    return result



def delete_user(email,username):

    query = f"""
    DELETE
    FROM users
    WHERE email = %s AND username = %s
    """

    db.connect()
    result = db.delete_row(query,(email,username))

    return result



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



def get_all_technologies():
    query = f"""
    SELECT * 
    FROM technologies
    """

    db.connect()
    result = db.select_rows(query)
    return result


def get_all_levels():
    query = f"""
    SELECT name 
    FROM levels
    """

    db.connect()
    result = db.select_rows(query)
    return result