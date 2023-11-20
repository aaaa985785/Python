# For Loop
# for variable in iterable:
#     do something here

for letter in "Hello World":
    print(letter.upper())

    if (letter == letter.upper()):
        print(letter)

myList = [1, 3, 5, 7, 9]

for num in myList:
    print(num**2)

# a list of tuples
for tuple in [(1, 2), (3, 5), (5, 7)]:
    print(tuple)

# tuples packing
for a, b in [(1, 2), (3, 5), (5, 7)]:
    print(a, b)
    print(a + b)

# dictionary (keys)
myDictionary = {"name": "Wilson", "age": 25}
# key
for item in myDictionary:
    print(item)
# value
for item in myDictionary.values():
    print(item)
# tuples
for item in myDictionary.items():
    print(item)
# # tuples packing
for key, value in myDictionary.items():
    print(f"The key is {key}")
    print(f"The value is {value}")

#set
for i in {1, 3, 5, 7, 9}:
    print(i)
