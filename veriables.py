# Variable = A container for a value - (string, integer, float, boolean)
# A variable behaves as if it was the value it contains
from statistics import quantiles

### Strings
first_name = "Sabbir"
last_name = "Nasir"
food = "Pizza"
email = "sabbir26@gmail.com"

# f-string - to use formatted string literals
print(f"Hello, {first_name} {last_name}")
print(f"You like {food}")
print(f"Your email address: {email}")

### Integers
age = 26
quantity = 3
number_of_students = 40

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {number_of_students} students.")

### Float
price = 10.69
gpa = 3.62
distance = 5.5
print(f"The price of the food is: {price}.")
print(f"Your CGPA is: {gpa}.")
print(f"You need to run at least {distance} km/per day.")

### Booleans
is_student = False
for_sale = True
is_online = False

print(f"Are you a student? -- {is_student}")
if is_student:
    print("You are a student!")
else:
    print("You are not a student!")

if for_sale:
    print("That item is for sale!")
else:
    print("That item is not available!")

if is_online:
    print("You are online.")
else:
    print("You are not online.")