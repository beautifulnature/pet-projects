# collections: Arrays, Lists, Tuples
# tuples: immutable : syntax ()
# list: mutable : syntax []
# multiple items

# a = 5
# b = "foo"

# tuple
# persons = ("brain", "bob", "alice", "jean")
# print(persons)
# print(persons[0])
# print(len(persons))
# print(persons[-1])

# for i in range(0, len(persons)):
#     # print(persons[i])

# for person in persons:
#     print(person)

# values = range(0, 5)
# print(values[-1])

# lists
persons = ["brain", "bob", "alice", "jean"]
new_person = "david"
persons.append(new_person)
# print(persons)
# print(persons[0])
# print(len(persons))
# print(persons[-1])

# for i in range(0, len(persons)):
#     # print(persons[i])

# persons[0] = "nag"
# print(persons)

# for person in persons:
#     print(person)

# def change_value(a):
#     a = 10
#     print(a)

# test = 5
# change_value(5)
# print(test)

# def change_value(a):
#     a[0] = 10

# test = [1, 2, 3, 4]
# print(test)
# change_value(test)
# print(test)

# tuples and functions
# def get_information():
#     return "alice", 20, 1.6

# def display_info(name, age, height):
#     print(f"name: {name}, age: {age}, height: {height}")

# infos = get_information()
# print(infos)
# print("name: ", infos[0])
# print("age: ", infos[1])
# print("height: ", infos[1])

# name, age, height = get_information()
# infos = get_information()
# display_info(name, age, height)
# display_info(*infos) # unpack tuple

print(persons)

# for person in persons[:-1]:
#     print(person)

name = "alice"
print(name[2:])
