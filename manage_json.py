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

def transform_json_structure():
    with open('survey_responses.json', 'r') as f:
        data = json.load(f)
    
    result = {}
    
    for item in data:
        date = item.pop('date')
        
        if date not in result:
            result[date] = {}
        
        result[date].update(item)
    
    with open('survey_unified.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Transformed JSON written to survey_unified.json")

