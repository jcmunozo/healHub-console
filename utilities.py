from datetime import datetime, timedelta

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

def medication_survey():
    # Medication and doses section
    medications = {}
    while True:
        med_name = input("\U0001F48A Ingrese el nombre del medicamento (o presione Enter para finalizar): \n\t")
        if med_name == "":
            break
        doses = []
        dose_count = 1
        while True:
            dose = input(f"\U0001F552 Ingrese la dosis {dose_count} para {med_name} formato dosis-hora ej. 1-6:30pm (o presione Enter para finalizar): \n\t")
            if dose == "":
                break
            doses.append(dose)
            dose_count += 1
        medications[med_name] = doses
    medications['date'] =  (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    return medications
    
