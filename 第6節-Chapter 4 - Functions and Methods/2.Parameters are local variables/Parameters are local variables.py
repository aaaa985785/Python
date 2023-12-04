# paramter(參數)、argument
# x, y are the parameters
def addition(x, y):
    print(x + y)


# 15, 20 are the arguments
addition(15, 20)

# 也可以這樣
a = 30
b = 25


def additions(x, y):
    print(x + y)


additions(a, b)  # arguments can be variables as well

# local variables, global variables
a = 5  # global variable


def f1():
    x = 2  # f1 function's local variable
    y = 3  # f1 function's local variable
    print(x, y, a)


def f2():
    x = 10  # f2 function's local variable
    y = 17  # f2 function's local variable
    print(x, y, a)


f1()
f2()

# copy by value
a = 10

# parameters (inputs) are Local variables in the function


def change(num):
    # num = a (copy by value) => num = 10
    num = 25


change(a)
print(a)  # 10

# copy by reference
a = [1, 2, 3, 4]


def change(list):
    # list = a(copy by reference) lst = a
    list[0] = 100  # a = [100, 2, 3, 4]


change(a)
print(a)

# can we ever change any copy by value global variables?
a = 10


def change(num):
    global a
    a = 25


change(a)
print(a)


# 自訂義 help() 的意思
def myAddition(a, b):
    """This function does addtion for inputs a and b"""
    print(a + b)


help(myAddition)
