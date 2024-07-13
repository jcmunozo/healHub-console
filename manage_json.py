import json
import os
from datetime import datetime
from datetime import timedelta
from messages import error_msg, successfull_msg

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
    try:
        with open('survey_responses.json', 'r') as f:
            data = json.load(f)
    except:
        return error_msg()

    if len(data) > 2 or len(data)<2:
        return error_msg()

    date =  (datetime.now()- timedelta(days=1)).strftime("%Y-%m-%d")

    result = {}
    final = {}

    for item in data:
        result.update(item)

    final[date] = sort_data(result)

    with open('survey_unified.json', 'w') as f:
        json.dump(final, f, indent=2)
    
    successfull_msg()    
    os.remove('survey_responses.json')

def sort_data(data):
    keys = data.keys()
    sorted_keys = sorted(keys)

    sorted_data = {}
    for key in sorted_keys:
        sorted_data[key] = data[key]
    return sorted_data
