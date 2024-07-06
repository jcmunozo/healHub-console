from datetime import datetime
from manage_json import load_existing_responses, save_to_json

class Survey:
    def __init__(self, questions):
        self.questions = questions
        self.responses = load_existing_responses()


    def conduct_survey(self):
        response = {}
        for question in self.questions:
            answer = question.answers()
            response[f"Q{question.id}"] = answer
        
        response['date'] =  datetime.now().strftime("%Y-%m-%d")
 
        self.responses.append(response)

    def execute_survey(self):
        # Conduct the survey
        self.conduct_survey()

        # Save responses to JSON file
        save_to_json('survey_responses.json', self.responses)

