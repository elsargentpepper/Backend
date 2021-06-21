from app.utils.users import get_technology_name 

def badge_identification(progresses,user):
    for progress in progresses:

        if progress["percentage"] >= 15 and progress["percentage"] < 30:

            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_junior"

            if badge_name in user["badges"]:
                pass
            else:
                user["badges"].append(badge_name)

        if progress["percentage"] >= 30 and progress["percentage"] < 45:

            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_junior_advanced"

            if badge_name in user["badges"]:
                pass
            else:
                user["badges"].append(badge_name)

        if progress["percentage"] >= 45 and progress["percentage"] < 60:
            
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_mid"
            
            if badge_name in user["badges"]:
                pass
            else:
                user["badges"].append(badge_name)

        if progress["percentage"] >= 60 and progress["percentage"] < 75:
             
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_mid_advanced"
            
            if badge_name in user["badges"]:
                pass
            else:
                user["badges"].append(badge_name)

        if progress["percentage"] >= 75 and progress["percentage"] < 90:
             
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_senior"
            
            if badge_name in user["badges"]:
                pass
            else:
                user["badges"].append(badge_name)

        if progress["percentage"] >= 90 and progress["percentage"] < 100:
                         
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_senior_advanced"
            
            if badge_name in user["badges"]:
                pass
            else:
                user["badges"].append(badge_name)

        if progress["percentage"] == 100:
                         
            tech_name = get_technology_name(progress["technology"])
            badge_name = f"{tech_name}_legend"
            
            if badge_name in user["badges"]:
                pass
            else:
                user["badges"].append(badge_name)

    return user