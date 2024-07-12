import sys
from survey import Survey
from messages import welcome_msg, bye_msg 
from medication import medication_survey
from manage_json import load_existing_responses, save_to_json, transform_json_structure
from creator import create_night_questions, create_day_questions 
from validators import valid_question_time 

if __name__ == '__main__':
    welcome_msg()

    while True:

        question_time = valid_question_time()
    
        questions = []

        if question_time == '3':
            results = medication_survey()
            responses_med = load_existing_responses(True)
            responses_med.append(results)
            save_to_json('medication_responses.json', responses_med)
        elif question_time == '4':
            transform_json_structure()
        elif question_time in ['1','2']:
            if question_time == '1':
                questions = create_day_questions()
            else:
                questions = create_night_questions()
            
            # Create survey instance
            daily_survey = Survey(questions)

            daily_survey.execute_survey()

        else:
            bye_msg()
            sys.exit()
