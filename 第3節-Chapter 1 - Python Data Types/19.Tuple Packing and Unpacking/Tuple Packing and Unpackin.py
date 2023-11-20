# 1. Tuple Packing
x = 10, 15, 17, 100  # tuple packing
print(x)
print(type(x))

# 2. Tuple Unpacking
x = ("Wilson", 25)
# 不好的寫法，當代碼多的時候不好維護
print(x[0])
print(x[1])
# 使用 Tuple Unpacking
name, age = x
print(name)
print(age)
# 其他使用
a, b = (15, 100)
print(a)
print(b)

# Packing and Unpacking 實用的例子 講兩個變數值對調
# 其他程式的寫法 新增暫時的變數(temp)
x = 25
y = 35

temp = x
x = y
y = temp

print(x)
print(y)
# 在 Python 中只要這樣
x, y = y, x

print(x)
print(y)
