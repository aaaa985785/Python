# Arbitrary(任意的) Number of Arguments


#  會有一個情況就是 sum(a,b) 但是 想要放入 sum(10, 15, 20, 25) 更多的數字 這樣只能用以下這樣操作
def sum(a, b):
    return a + b


r1 = sum(10, 15)
r2 = sum(r1, 20)
r3 = sum(r2, 25)
print(r3)


# 但是以上這樣的做法不是一個好辦法，所以要有 任意數的定義 input 使用 *args 打包成 tuple
def sum(*args):
    print(args)
    print(type(args))


sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# 這樣就可以算出 1 + .... + 10
# 有兩種寫法 第一種
def sum(*args):
    result = 0
    for number in range(0, len(args)):
        print(f"We are now at number {number}.")
        print(f"Also, args[number is {args[number]}]")
        result += args[number]
        print(f"Now, the resule is {result}")
    return result


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 使用 **kwargs 放入 dict
def myfunc(**kwargs):
    print(kwargs)
    print(type(kwargs))


myfunc(name="Wilson", age=25, address="Hawaii")


# 就可以這樣
def myfunc(**kwargs):
    print("{} is now {} years old.".format(kwargs["name"], kwargs["age"]))


myfunc(name="Wilson", age=25, address="Hawaii")


# They can be used in one function at the same time as well(他們倆個可以同時放在function中)
def myfunc(*args, **kwargs):
    print("I would like to eat {} {}".format(args[1], kwargs["food"]))


myfunc(14, 17, 23, name="jack", food="eggs")


# 要注意順序 如果再定義 function 而下面的4個都要用的的話 就要按照下面順序 Function input definition order should be
# 1. normal parameters (p1, p2)
# 2. default parameters p3="three"
# 3. *args
# 4. **kwargs
def func(p1, p2, p3="three", *args, **kwargs):
    print("---------------------------------")
    print(p1, p2, p3, args, kwargs)


func(1, 2, 3, 4, 5, x=1, y=3)
func(1, 2, 3, 4, x=4)
func(1, 2, 3, 4)
func(1, 2, 3)
func(1, 2)
# func(1)
