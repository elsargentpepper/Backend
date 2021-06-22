def technologies_formating(technologies):

    json = dict()
    json["response"] = list()

    for technology in technologies:
        tech = dict()

        tech["name"] = technology[1]
        tech["image"] = technology[2]
        tech["summary"] = technology[3]

        json["response"].append(tech)

    return json