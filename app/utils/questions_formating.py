import random

def questions_formating(questions,number_of_questions):
    random.shuffle(questions)
    json_response = dict()
    json_response['questions'] = list()
    for question in questions[:number_of_questions]:
        json = dict()
        json['question'] = question[0]
        correct_answer = question[3]
        random.shuffle(question[1])
        json['answers'] = question[1]
        json['correct_answer_index'] = question[1].index(correct_answer)
        json['image'] = question[2]
        json_response['questions'].append(json)
    return json_response

def add_format_question(question):

    for i in range(0,len(question.answers)):
        question.answers[i] = question.answers[i].replace("'","''")

    question.question = question.question.replace("'","''")

    question.right_answer.replace("'","''")

    return question