# logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

temp = 25
is_raining = True

if temp > 35 or  temp <0 or is_raining:
    print("The out door event is cancelled!")
else:
    print("The outdoor event is still on!")

temp2 = 30
is_sunny = True

if temp2 >= 28 and is_sunny:

    print("It is HOT outside!")
    print("It is Sunny outside!")
elif temp2 <= 0 and is_sunny:
    print("It is cold outside!")
    print("It is Sunny outside!")
elif temp2 < 28 and temp > 0 and is_sunny:
    print("It is warm outside!")
    print("It is Sunny outside!")
else:
    print("It is Not Hot not Sunny outside!")

temp3 = 10
is_sunny2 = False

if temp3 >= 28 and is_sunny2:
    print("It is HOT outside!")
    print("It is Sunny outside!")
elif temp3 <= 0 and not is_sunny2:
    print("It is cold outside!")
    print("It is cloudy outside!")
elif temp3 < 28 and temp > 0 and not is_sunny2:
    print("It is warm outside!")
    print("It is cloudy outside!")
else:
    print("It is Not Hot not Sunny outside!")
