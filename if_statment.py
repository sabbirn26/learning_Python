# if = Do some code only IF some condition is TRUE
#      else do something else

### EX- 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are now signed up! ")
elif age < 0:
    print("You are not born yet!")
elif age >= 100:
 print("You are too old mate!")
else:
    print("You must be at least 18!")

### EX- 2
response = input("Would you like food? (Y/N) ")
if response == "Y":
    print("Have some food mate!")
else:
    print("No food for you mate!")

### EX- 3
name = input("Enter your name: ")
if name == "":
    print("You did not type your name!")
else:
    print(f"Your name is: {name}")

### EX- 4
for_sale = True
if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")

### EX- 5
online = False
if online:
    print("The user is online")
else:
    print("The user is offline")
