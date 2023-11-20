# len()
myTuple = (10, "100", "Hello")
print(len(myTuple))

# indexing rule
print(myTuple[0])
print(myTuple[0:2])

# count()
print(myTuple.count(10))

# index()
print(myTuple.index("Hello"))

# 因為是 immutable，所以 pop, append, sort..之類會改變內容的都不能使用
# myTuple.append(150)
myTuple[1] = 100
print(myTuple)
