from survey import Survey

# Define survey questions
questions = [
    "En la mañana al despertar siento que me puedo mover desde el primer momento. (1-10)",
    "Me siento de buen ánimo y con energía la mayor parte del tiempo.  (1-10)",
    "Duermo toda la noche de corrido, sin interrupciones y siento que he descansado al despertar.  (1-10)",
    "Puedo realizar las actividades de la vida diaria sin dificultad y sin ayuda (ej. comer, bañarme, vestirme).   (1-10)",
    "Puedo caminar sin dificultad y sin ayuda. (1-10)",
    "Dolor, siendo 1 que no ha sentido dolor y 10 que ha sentido el peor dolor de su vida. (1-10)",
    "¿Ha presentado algun síntoma molesto respecto a su tratamiento? (Si/No) Si si, por favor describalo:",
]

# Create survey instance
daily_survey = Survey(questions)

# Conduct the survey
print("Bienvenido a healHub-console")
daily_survey.conduct_survey()

# Save responses to JSON file
daily_survey.save_to_json('survey_responses.json')

print("Gracias por completar la encuesta diaria. Sus respuestas han sido guardadas.")

print("Sesion terminada. Todas las respuestas estan en survey_responses.json")
    
print("Hasta pronto")
