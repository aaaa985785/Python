# (Bonus) Assignment and Local Variable
a = "hello"


def change():
    print(a)  # Python created "a" Local variable
    a = 2  # a variable assignment


change(
)  # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

# 第二個例子
b = "apple"


def chanege(x):
    if x:
        b = "we just changed a"  # vaiable assignment
    print(b)


chanege(
    False
)  # UnboundLocalError: cannot access local variable 'b' where it is not associated with a value
