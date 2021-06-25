from typing import List


def user_format(user):
    json = dict()
    json["id"] = user[0]
    json["name"] = user[1]
    json["email"] = user[2]
    json["username"] = user[3]
    json["password"] = user[4]
    json["login_type"] = user[5]
    if user[6] != None:
        json["badges"] = user[6]
    else:
        json["badges"] = list()
    if user[7] != None:
        json["prefered_technologies"] = user[7]
    else:
        json["prefered_technologies"] = list()
    json["profile_pic"] = user[8]
    return json

def users_format(users):
    json = dict()
    json["users"] = list()
    for user in users:
        json["users"].append(user_format(user))
    return json

def user_format_body(user):
    json = dict()
    json["id"] = user.id
    json["name"] = user.name
    json["email"] = user.email
    json["username"] = user.username
    json["password"] = user.password
    json["login_type"] = user.login_type
    json["badges"] = user.badges
    json["prefered_technologies"] = user.prefered_technologies
    json["profile_pic"] = user.profile_pic
    return json