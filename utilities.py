
def welcome_msg():
    print("\n" + "=" * 50)
    print("BIENVENIDO A \U0001F9E0".center(50, " "))
    print("=" * 50)
    print("      __ __              __   __ __         __ ")
    print("     / // / ___  ___ _  / /  / // / __ __  / / ")
    print("    / _  / / -_)/ _ `/ / /  / _  / / // / / _ \\")
    print("   /_//_/  \\__/ \\_,_/ /_/  /_//_/  \\_,_/ /_.__/\n")
    print(" consola ".center(50, "*"))
    print("\n","Tu salud importa! Empecemos ... \U0001F680".center(50, " "), "\n")
    print("=" * 50, "\n")

def bye_msg():
    print("\nGracias por completar la encuesta diaria \U0001F601 . Sus respuestas han sido guardadas \U0001F37B.")
    print("\nSesion terminada \U0001F389. Todas las respuestas estan en survey_responses.json \U0001F510")
    print("\nHasta pronto \U0000270C  \U0001F9EC \n")

def is_valid_number(value):
    try:
        if int(value) < 1 or int(value) > 10:
            return "\n\t \U0000274C Uups has ingresado un numero fuera de rango. Por favor intentalo de nuevo.\n"
        return "Ok"
    except ValueError:
        return "\n\t \U0000274C Uups has ingresado una palabra en lugar de un numero. Por favor intentalo de nuevo.\n"


def is_valid_string(value):
    if value.lower() in ["si", "sí", "no"]:
        return "Ok"
    else:
        return "\n\t \U0000274C Por favor digite Sí o No he intentalo de nuevo.\n"

def answers(question, question_type):
    while True:
        answer = input(question)
        if question_type == 1:
            result = is_valid_number(answer)
            if result == "Ok":
                return answer
            else:
                print(result)
        elif question_type in [2, 3]:
            result = is_valid_string(answer)
            if result == "Ok" and answer.lower() in ["si", "sí"]:
                if question_type == 2:
                    return input("\n\t\U0001F50D Por favor diganos cuales:\n\t")
                else:
                    while True:
                        value = input("\n\t\U0001F50D Cuantas? (1-10)\n\t")
                        var = is_valid_number(value)
                        if var == "Ok":
                            return value
                        else:
                            print(var)
            elif result == "Ok":
                return(answer)
            else:
                print(result)
        else:
            return answer

# TODO: Function to valid the format of the questions that required anwers like this "1-6:30am"
# def is_valid_format(value):
