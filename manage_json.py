import json
import os

def load_existing_responses(ismed=False):

    filename = ' '
    
    if ismed:
        filename = 'medication_responses.json'
    else:
        filename = 'survey_responses.json'

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_to_json(filename, responses):
    with open(filename, 'w') as f:
        json.dump(responses, f, indent=2)

