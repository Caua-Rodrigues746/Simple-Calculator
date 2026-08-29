try:
    first_number = float(input("Inform the first number!: "))
    second_number = float(input("Inform the second number!: "))
except Exception:
    print("Thats not a number!")


operation = input("Inform the operation method!")

if operation == "+":
    math = first_number + second_number
    print("The result is: " + str(math))
elif operation == "-":
    math = first_number - second_number
    print("the result is: " + str(math))
elif operation == "*":
    math = first_number * second_number
    print("The result is: " + str(math))
elif operation == "/":
    math = first_number / second_number
    print("The result is: " + str(math))
else:
    print("Thats not an operation method")