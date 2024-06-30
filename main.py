from survey import Survey
from utilities import welcome_msg, bye_msg

# Define survey questions
questions = {
    "En la mañana al despertar siento que me puedo mover con facilidad desde el primer momento. (1-10)": 1,
    "Me siento de buen animo y con energía la mayor parte del tiempo. (1-10)": 1,
    "Duermo toda la noche de corrido, sin interrupciones y siento que he descansado al despertar. (1-10)": 1,
    "Puedo realizar las actividades de la vida diaria sin dificultad y sin ayuda (ej. comer, banarme, vestirme). (1-10)": 1,
    "Puedo caminar sin dificultad y sin ayuda. (1-10)": 1,
    "Dolor, siendo 1 que no ha sentido dolor y 10 que ha sentido el peor dolor de su vida. (1-10)": 1,
    "¿Ha presentado algún síntoma molesto respecto a su tratamiento? (Sí/No)": 2,
    "¿Cuantas veces se desperto?, por favor digite la hora en la que se desperto (ej. 1:40am)": 4,
    "Rigidez, siendo 1 nada de rigidez y 10 mucha rigidez. (1-10)": 1,
    "Pesadillas?. (Sí/No)": 3,
    "Observaciones. (Sí/No)": 2
}


if __name__ == '__main__':
    welcome_msg()

    # Create survey instance
    daily_survey = Survey(questions)

    # Conduct the survey
    daily_survey.conduct_survey()

    # Save responses to JSON file
    daily_survey.save_to_json('survey_responses.json')

    bye_msg()
