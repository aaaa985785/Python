# + concatenation
myString1 = "Hello, "
myString2 = "my name is Wilson"
result = myString1 + myString2

print(result)

# cannot make concatenation on Strings and numbers.
myString1 = "Hello"
myNumber1 = 1

# print(myString1 + myNumber1)  # can only concatenate str (not "int") to str

# String is immutable(不可改變)
myString1 = "Hello"
myString1[0] = "h"
print(myString1)  # 'str' object does not support(支援) item assignment
