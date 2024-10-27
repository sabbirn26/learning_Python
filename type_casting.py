# Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Sabbir Nasir"
age = 26
gpa = 3.62
is_student = False

print(type(name)) #---> <class 'str'>
print(type(age)) #---> <class 'int'>
print(type(gpa)) #---> <class 'float'>
print(type(is_student)) #---> <class 'bool'>

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = float(age)
print(age)
print(type(age))

age = str(age)
print(age)
print(type(age))

age += "1"
print(age)

name = bool(name)
print(name)