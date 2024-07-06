from datetime import datetime, timedelta
from manage_json import load_existing_responses

class Survey:
    def __init__(self, questions):
        self.questions = questions
        self.responses = load_existing_responses()


    def conduct_survey(self):
        print(type(self.responses))
        response = {}
        for question in self.questions:
            answer = question.answers()
            response[f"Q{question.id}"] = answer
        
        response['date'] =  (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
 
        self.responses.append(response)

