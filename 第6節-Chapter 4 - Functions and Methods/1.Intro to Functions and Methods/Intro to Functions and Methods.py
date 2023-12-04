# help()
myList = [1, 2, 3, 4]
myList.insert(2, 10)
help(myList.insert)


# def(定義)
def sayHi():
    print("Hello, how are you?")


# function execution, invokation
sayHi()

print(sayHi)  # <function sayHi at 0x000001F507FAF060>


# input 括號內的值叫做 parameter
def addition(x, y):
    print(x + y)


addition(6, 8)
