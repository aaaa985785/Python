# Functions are Objects
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


addition = subtraction

print(addition(10, 5))

# 要避免 內建函式 名稱 當變數名 不然會被取代
str = "This is my string"
x = 25

print("hello" + str(x))  # TypeError: 'str' object is not callable
