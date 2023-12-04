# Positional and Keyword Arguments(參數)
def exponent(a, b):
    return a**b


# positional arguments
print(exponent(2, 3))  # 8
print(exponent(3, 2))  # 9

# keyword arguments
print(exponent(a=10, b=2))
# 這樣就算a,b位置對調也不會影響
print(exponent(b=2, a=10))

# keyword 之前課程有用過
myList = [4, 6, 3, 2, 1]
print(sorted(myList, reverse=True))
# myList is positional argument
# reverse=False is keyword argument
