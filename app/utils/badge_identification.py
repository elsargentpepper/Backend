from app.utils.connections.technologies import get_technology_name 

def badge_identification(progresses,user):

    for progress in progresses:

        if progress["percentage"] == 15:

            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_junior"

            user = badge_check(user,badge_name)
                

        if progress["percentage"] == 30 :

            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_junior_advanced"

            user = badge_check(user,badge_name)


        if progress["percentage"] == 45 :
            
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_mid"
            
            user = badge_check(user,badge_name)


        if progress["percentage"] == 60 :
             
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_mid_advanced"
            
            user = badge_check(user,badge_name)


        if progress["percentage"] == 75:
             
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_senior"
            
            user = badge_check(user,badge_name)


        if progress["percentage"] == 90:
                         
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_senior_advanced"
            
            user = badge_check(user,badge_name)


        if progress["percentage"] == 100:
                         
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_legend"
            
            user = badge_check(user,badge_name)


    return user


def badge_check(user,badge_name):

    if not badge_name in user["badges"]:

        user["badges"].append(badge_name)

    return user
