# Python Calculator

operator = input("Enter and operator (+ - * /): ")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if operator == "+":
    result = number1 + number2
    print(round(result, 3))
elif operator == "-":
    result = number1 - number2
    print(round(result, 3))
elif operator == "*":
    result = number1 * number2
    print(round(result, 3))
elif operator == "/":
    result = number1 / number2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator. Please enter the correct operator, and try again!")