# Lambda Expression
# Lambda variable: operation  直接自帶 return 效果
result = (lambda x: x**2)(5)
print(result)

# Lambda input1, input2, ....: operation  直接自帶 return 效果
myTuple = (lambda x, y: (x + y, x - y))(15, 30)
print(myTuple[0])
print(myTuple[1])

# 用在higher-order
for item in map(lambda x: x**2, [15, 10, 5, 0]):
    print(item)

for item in filter(lambda x: x % 2 == 0, [15, 10, 5, 0]):
    print(item)
