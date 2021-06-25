from app.utils.connections.questions import get_all_questions_tech

def question_validation(question_given):
    questions = get_all_questions_tech(question_given.technology)
    for question in questions:
        print(question[5])
        if question_given.question == question[5] and question_given.answers == question[1] and question_given.right_answer == question[6] and question_given.image == question[2]:
            return True

    return False