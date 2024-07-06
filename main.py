import sys
from question import Question
from survey import Survey
from messages import welcome_msg, bye_msg, menu
from utilities import medication_survey
from manage_json import load_existing_responses, save_to_json

def create_day_questions():

    q1 = Question("En la mañana al despertar siento que me puedo mover con facilidad desde el primer momento. (1-10)",1,1)
    q2 = Question("Duermo toda la noche de corrido, sin interrupciones y siento que he descansado al despertar. (1-10)",1,3)
    q3 = Question("¿Cuantas veces se desperto?, por favor digite la hora en la que se desperto (ej. 1:40am)",4,8)
    q4 = Question("¿Ha presentado algún síntoma molesto respecto a su tratamiento? (Sí/No)",2,7)
    q5 = Question("Pesadillas?. (Sí/No)",3,10)

    return [q1,q2,q3,q4,q5]

def create_night_questions():

    q6 = Question("Puedo realizar las actividades de la vida diaria sin dificultad y sin ayuda (ej. comer, banarme, vestirme). (1-10)", 1,4)
    q7 = Question("Me siento de buen animo y con energía la mayor parte del tiempo. (1-10)",1,2)
    q8 = Question("Puedo caminar sin dificultad y sin ayuda. (1-10)",1,5)
    q9 = Question("Dolor, siendo 1 que no ha sentido dolor y 10 que ha sentido el peor dolor de su vida. (1-10)",1,6)
    q10 = Question("Rigidez, siendo 1 nada de rigidez y 10 mucha rigidez. (1-10)",1,9)
    q11 = Question("Observaciones. (Sí/No)",2,11)

    return [q6,q7,q8,q9,q10,q11]

def execute_survey(questions):
    # Create survey instance
    daily_survey = Survey(questions)

    # Conduct the survey
    daily_survey.conduct_survey()

    # Save responses to JSON file
    save_to_json('survey_responses.json', daily_survey.responses)


if __name__ == '__main__':
    welcome_msg()

    while True:

        response = menu()

        questions = []

        if response == '1':
            questions = create_day_questions()
            execute_survey(questions)
        elif response == '2':
            questions = create_night_questions()
            execute_survey(questions)
        elif response == '3':
            results = medication_survey()
            responses_med = load_existing_responses(True)
            responses_med.append(results)
            save_to_json('medication_responses.json', responses_med)
        else:
            bye_msg()
            sys.exit()
