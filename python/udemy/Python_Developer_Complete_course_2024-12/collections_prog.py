# collections: Arrays, Lists, Tuples
# tuples: immutable : syntax ()
# list: mutable : syntax []
# multiple items

# a = 5
# b = "foo"

# persons = ("brain", "bob", "alice", "jean")
persons = ["brain", "bob", "alice", "jean"]
# print(persons)
# print(persons[0])
# print(len(persons))
print(persons[-1])

# for i in range(0, len(persons)):
#     # print(persons[i])

for person in persons:
    print(person)

values = range(0, 5)
print(values[-1])