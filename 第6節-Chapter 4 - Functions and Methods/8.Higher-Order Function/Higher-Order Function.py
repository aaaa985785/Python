# Higher-Order Function
def higherOrder(fn):
    fn()


def smallfunc():
    print("hello from small funciton.")


higherOrder(smallfunc)


# 1. map() map(func, iterable)
def square(num):
    return num**2


myList = [10, 3, 9, 8, 10]
print(map(square, myList))

for item in map(square, myList):
    print(item)


# 2. filter() filter(func, iterable) 第一個function 某些 return true 某些 return false，iterable就要判斷true加進來
def even(num):
    return num % 2 == 0


myList = [444532, 3211543, -998432, 66154]
for item in filter(even, myList):
    print(item)
