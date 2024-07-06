from messages import menu

def is_valid_number(value, initial, final):
    try:
        if int(value) < initial or int(value) > final:
            return "\n\t \U0000274C Uups has ingresado un numero fuera de rango. Por favor intentalo de nuevo.\n"
        return "Ok"
    except ValueError:
        return "\n\t \U0000274C Uups has ingresado una palabra en lugar de un numero. Por favor intentalo de nuevo.\n"


def is_valid_string(value):
    if value.lower() in ["si", "sí", "no"]:
        return "Ok"
    else:
        return "\n\t \U0000274C Por favor digite Sí o No he intentalo de nuevo.\n"

def valid_question_time():
    while True:
        menu()
        response = input("\U0001F48A Ingrese la opcion deseada por favor: \n\t")
        result = is_valid_number(response,1,5)
        if result == "Ok":
            return response
        else:
            print(result)
