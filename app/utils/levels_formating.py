def levels_formating(info):

    json = dict()
    json["response"] = list()

    for entry in info:
        json["response"].append(entry[0])
    
    return json