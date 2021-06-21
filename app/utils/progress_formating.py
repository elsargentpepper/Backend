def progress_format(user):
    json = dict()
    json["progres_id"] = user[0]
    json["percentage"] = user[1]
    json["user_id"] = user[2]
    json["technology"] = user[3]
    return json

def progresses_format(users):
    json = dict()
    json["users_progresses"] = list()
    for user in users:
        json["users_progresses"].append(progress_format(user))
    return json