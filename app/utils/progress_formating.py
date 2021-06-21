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

def progress_percentage_formating(progresses):
    response = dict()
    response['response'] = list()
    for progress in progresses:
        json = dict()
        json["name"] = progress[1]
        json["percentage"] = progress[0]
        response['response'].append(json)
    return response