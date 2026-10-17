import calculator_functions

def ask_question():
    question = input("Do you want to perform another operation? type Yes or No! ").lower()
    return question

numbers = [ ]

while True:
    try:
        ask_numbers = float(input("Tell me the numbers you want for the math! type anything else to stop!: "))
        numbers.append(ask_numbers)

    except ValueError:
        operation_type = input("Which operation type do you want? + - / * ")

        try:
            if operation_type == "+":
                result = calculator_functions.addition(numbers)

                print(f"The result is {result}")

                another_operation = ask_question()

                answer = calculator_functions.question_answer(another_operation)

                if answer == True:
                    numbers.clear()
                    continue

                else:
                    break
                
            elif operation_type == "*":
                result = calculator_functions.multiplication(numbers)

                print(f"The result is {result}")

                another_operation = ask_question()

                answer = calculator_functions.question_answer(another_operation)

                if answer == True:
                    numbers.clear()
                    continue

                else:
                    break

            elif operation_type == "/":
                result = calculator_functions.division(numbers)

                print(f"The result is {result}")

                another_operation = ask_question()

                answer = calculator_functions.question_answer(another_operation)

                if answer == True:
                    numbers.clear()
                    continue

                else:
                    break

            elif operation_type == "-":
                result = calculator_functions.subtraction(numbers)

                print(f"The result is {result}")

                another_operation = ask_question()

                answer = calculator_functions.question_answer(another_operation)

                if answer == True:
                    numbers.clear()
                    continue

                else:
                    break

            else:
                print("It must be an operation type!")
                break
        
        except ZeroDivisionError:
            print("Thats not possible to calculate!")
            break