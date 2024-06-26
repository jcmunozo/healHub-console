from survey import Survey

# Define survey questions
questions = [
    "En la mañana al despertar siento que me puedo mover desde el primer momento. (1-10)",
    "Me siento de buen animo y con energía la mayor parte del tiempo. (1-10)",
    "Duermo toda la noche de corrido, sin interrupciones y siento que he descansado al despertar. (1-10)",
    "Puedo realizar las actividades de la vida diaria sin dificultad y sin ayuda (ej. comer, banarme, vestirme). (1-10)",
    "Puedo caminar sin dificultad y sin ayuda. (1-10)",
    "Dolor, siendo 1 que no ha sentido dolor y 10 que ha sentido el peor dolor de su vida. (1-10)",
    "¿Ha presentado algún síntoma molesto respecto a su tratamiento? (Sí/No) Si si, por favor describalo:",
    "¿Cuantas veces se desperto?",
    "Rigidez, siendo 1 nada de rigidez y 10 mucha rigidez. (1-10)",
    "Pesadillas?. (Sí/No) cuantas",
    "Observaciones"
]

# Create survey instance
daily_survey = Survey(questions)

# Conduct the survey

print("\n" + "=" * 50)
print("       BIENVENIDO A ")
print("=" * 50)
print("      __ __              __   __ __         __ ")
print("     / // / ___  ___ _  / /  / // / __ __  / / ")
print("    / _  / / -_)/ _ `/ / /  / _  / / // / / _ \\")
print("   /_//_/  \\__/ \\_,_/ /_/  /_//_/  \\_,_/ /_.__/")
print("\n" + "*" * 20 + " consola " + "*" * 20)
print("\nTu salud importa! Empecemos con el checkeo diario.")
print("-" * 50)

daily_survey.conduct_survey()

# Save responses to JSON file
daily_survey.save_to_json('survey_responses.json')

print("Gracias por completar la encuesta diaria. Sus respuestas han sido guardadas.")

print("Sesion terminada. Todas las respuestas estan en survey_responses.json")
    
print("Hasta pronto")
