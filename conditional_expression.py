# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 5
print("Positive!" if num > 0 else "Negative!")

num2 = 6
result = "Even!" if num2 % 2 == 0 else "Odd!"
print(result)

a = 6
b = 7

max_num = "a is the bigger number!" if a > b else "b is the bigger number!"
min_num = "a is the small number!" if a < b else "b is the small number!"

print(max_num)
print(min_num)

age = 25
status = "Adult!" if age >= 18 else "Underage!"
print(status)

temp = 30
weather = "Weather is Hot!" if temp > 20 else "Weather is cold!"
print(weather)

user_role = "admin"
access_level = "User has full access!" if user_role == "admin" else "User has partial access!"
print(access_level)