def user_format(user):
    json = dict()
    json["id"] = user[0]
    json["name"] = user[1]
    json["email"] = user[2]
    json["username"] = user[3]
    json["password"] = user[4]
    json["login_type"] = user[5]
    json["badges"] = user[6]
    json["prefered_technologies"] = user[7]
    return json

def users_format(users):
    json = dict()
    json["users"] = list()
    for user in users:
        json["users"].append(user_format(user))
    return json