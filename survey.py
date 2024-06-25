import json
from datetime import datetime
import os

class Survey:
    def __init__(self, questions):
        self.questions = questions
        self.responses = self.load_existing_responses()

    def load_existing_responses(self):
        if os.path.exists('survey_responses.json'):
            with open('survey_responses.json', 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def conduct_survey(self):
        response = {}
        for index, question in enumerate(self.questions):
            answer = input(f"{question}: \n")
            response[f"Q{index + 1}"] = answer
        
        # Medication and doses section
        medications = {}
        while True:
            med_name = input("ingrese el nombre del medicamento (o presione Enter para finalizar): ")
            if med_name == "":
                break
            doses = []
            dose_count = 1
            while True:
                dose = input(f"Ingrese la dosis {dose_count} para {med_name} formato dosis-hora ej. 1-6:30pm (o presione Enter para finalizar): ")
                if dose == "":
                    break
                doses.append(dose)
                dose_count += 1
            medications[med_name] = doses
        
        response['medications'] = medications
        response['date'] = datetime.now().strftime("%Y-%m-%d")
        self.responses.append(response)

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.responses, f, indent=2)

