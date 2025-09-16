# print("hello")
# print()
# print("my name is foo")
# print("")
# print("yes, foo is my name")
# print("yes, it's my name")
# print('yes, it"s my name')

# name = "foo"
# print('my name is', name)
# print('my name is ' + "foo")
# print('my name is ' +  name)
# print(f'my name is {name}')

"""
multi line comment
multi line comment
multi line comment
multi line comment
multi line comment
multi line comment
"""

"""
name = input("what is your name? ")
try:
    age = int(input("what is your age? "))
except:
    print("ERROR: age must be a number")
else:
    print(f'hi {name}, you are {age} years old')
    print("hi " + name +", soon you will be " + str(age + 1) + " years old")
    print(f'hi {name}, soon you will be {age + 1} years old')
"""

# print(type(age))
# print('hi {name} ' + 'you are ' + age + ' years old')

## python programming cheat sheet
# variable types
# a = "hello"     # character string: str
# b = 5           # real number: int
# c = 1.5         # floating number: float
# d = True        # True or False: bool
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# print(a)
# print(b)
# print(c)
# print(d)

# print and input

# name = input("what is your name?")
# print("your name is " + name)           # string concatenation
# print(f"your name is {name}")           # formatted string or string interpolation
# print("your name is %s" %name)          # formatted string (old format)

# comments
# one line comments
"""
multi 
    line  
        comments
"""

# conversion
# age = 30
# print("your age is: " + str(age))       # conversion from int to str, and concatenation

# age_str = "30"
# age_str = "thirty"
# age_int = int(age_str)                  # conversion from str to int
                                        # use a try / except bloc to manage the errors / exceptions

# while loop
# loops while the condition is True

# name = ""
# while name == "":
#     name = input("what is your name?")

# loops a number of times
# for i in range(1, 4):
#     print(i)

# functions
# definiton
# def display_person_info(name, age, height=0):
#     print(f"hi {name}, your age is {age}")

# call
# display_person_info("nagaraju", 43)

# return: returns a value or exits the function

# conditions

# ==  # equal
# <=  # less or equal
# <   # less
# >=  # greater or equal
# >   # greater
# not # opposite

# if age == 17:
#     print("you are almost adult")
# elif 10 <= age < 18:
#     print("you are teenager")
# elif age >= 18:
#     print("you are an adult")
# else:
#     print("you are a minor")

# # exception
# try:
#     age_int = int(age_str)
# except:
#     print("ERROR: age must be a number")

# while loop
# n = 0

# while n < 5:
#     print(f'hi - {n}')
#     n = n + 1

# print("end of the loop")

# password = ""

# while password != "1234":
#     password = input("what is the password?")

# # while not password == "1234":
# #     password = input("what is the password?")

# print("password is correct. you have access to the account")

# ask for name
def ask_for_name():
    name = ""

    while name == "":
        name = input("what is your name?")
    return name

# age = 0

# ask for age
def ask_for_the_age(person_name):
    age = 0
    # global age
    while age == 0:
        age_str = input(person_name + " what is your age?")
        try:
            age = int(age_str)
        except:
            print("ERROR: age must be a number")
    return age

# name1 = ask_for_name()
# name2 = ask_for_name()

# ask_for_the_age()
# age1 = ask_for_the_age(name1)
# age2 = ask_for_the_age(name2)

# display results
# print(f"your name is {name1}, you are {age1} years old")
# print(f"soon you will be {age1 + 1}")
# print(f"your name is {name2}, you are {age2} years old")
# print(f"soon you will be {age2 + 1}")

def display_person_info(name, age, height=0):
    print()
    print(f"your name is {name}, you are {age} years old")
    print("your name is %s, you are %s years old" %(name, age))
    print(f"soon you will be {age + 1}")

    if age == 17:
        print("you are almost an adult")
    # elif age >= 10 and age < 18:
    elif 10 <= age < 18:
        print("you are a teenager")
    elif age == 18:
        print("you are now an adult: congrats!")
    elif age > 60:
        print("you are a senior")
    elif age > 18:
        print("you are an adult")
    elif age == 1 or age ==2:
        print("you are a baby")
    else:
        print("you are a kid")

    if not height == 0:
        print("your height: " + str(height) + "m")

# display_person_info(name1, age1)
# display_person_info(name2, age2)

NB_PERSONS = 1

for i in range(0, NB_PERSONS):
    # print(i)
    name = "foo" + str(i + 1)
    age =  ask_for_the_age(name)
    display_person_info(name, age)

print("""
A first line
    second line
        third line      
""")

print("first", 5, 5.99, "last")