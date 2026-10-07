numbers = [ ]

while True:
    try:
        ask_numbers = float(input("Tell me the numbers you want for the math! type anything else to stop!: "))
    
    except ValueError:
        operation_type = input("Which operation type do you want? + - / * ")
        
        if operation_type == "+":
            result = sum(numbers)
            
            print(f"The result is {result}")
            
            another_operation = input("Do you want to perform another operation? type Yes or No! ").lower()

            if another_operation == "no":
                break

            elif another_operation == "yes":
                print("Lets try again!")

            else:
                print("It must be Yes or No!")
                break

        if operation_type == "*":
            value = 1

            for number in numbers:
                value *= number
            
            print(f"The result is {value}")

            another_operation = input("Do you want to perform another operation? type Yes or No! ").lower()

            if another_operation == "no":
                break

            elif another_operation == "yes":
                print("Lets try again!")

            else:
                print("It must be Yes or No!")
                break

        if operation_type == "/":
            div_res = numbers[0]

            for number in numbers[1:]:
                div_res /= number

            print(f"The result is {div_res}")

            another_operation = input("Do you want to perform another operation? type Yes or No! ").lower()

            if another_operation == "no":
                break

            elif another_operation == "yes":
                print("Lets try again!")

            else:
                print("It must be Yes or No!")
                break

        if operation_type == "-":
            sub_res = numbers[0]

            for number in numbers[1:]:
                sub_res -= number

            print(f"The result is {sub_res}")

            another_operation = input("Do you want to perform another operation? type Yes or No! ").lower()

            if another_operation == "no":
                break

            elif another_operation == "yes":
                print("Lets try again!")

            else:
                print("It must be Yes or No!")
                break

        else:
            print("It must be an operation type!")

    numbers.append(ask_numbers)