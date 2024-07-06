from utilities import is_valid_number, is_valid_string

class Question:
    def __init__(self, question, q_type, id):
        self.question = question
        self.q_type = q_type
        self.id = id
  
    def answers(self):
        while True:
            answer = input(f"\U0001F4DD {self.question}: \n\t") 
            if self.q_type == 1:
                result = is_valid_number(answer,1,10)
                if result == "Ok":
                    return answer
                else:
                    print(result)
            elif self.q_type in [2, 3]:
                result = is_valid_string(answer)
                if result == "Ok" and answer.lower() in ["si", "sí"]:
                    if self.q_type == 2:
                        return input("\n\t\U0001F50D Por favor diganos cuales:\n\t")
                    else:
                        while True:
                            value = input("\n\t\U0001F50D Cuantas? (1-5)\n\t")
                            var = is_valid_number(value,1,5)
                            if var == "Ok":
                                return value
                            else:
                                print(var)
                elif result == "Ok":
                    return(answer)
                else:
                    print(result)
            else:
                return answer

    # TODO: Function to valid the format of the questions that required anwers like this "1-6:30am"
    # def is_valid_format(value):
