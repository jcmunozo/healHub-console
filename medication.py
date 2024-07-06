from datetime import datetime 

def medication_survey():
    # Medication and doses section
    total_date = {}
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
    date_med =  datetime.now().strftime("%Y-%m-%d")

    total_date[date_med] = medications
    
    return total_date
    
