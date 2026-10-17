def addition(numbers):
    operation = sum(numbers)
    return operation

def multiplication(numbers):
    value = 1
    for number in numbers:
        value *= number
    return value

def division(numbers):
    div_res = numbers[0]
    for number in numbers[1:]:
        div_res /= number
    return div_res

def subtraction(numbers):
    sub_res = numbers[0]
    for number in numbers[1:]:
        sub_res -= number
    return sub_res


def question_answer(another_operation):
    if another_operation == "no":
        return False
        
    elif another_operation == "yes":
        print("Lets try again!")
        return True

    else:
        print("It must be Yes or No!")
        return False
        