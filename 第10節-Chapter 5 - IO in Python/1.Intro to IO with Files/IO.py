# I/O with Files(.txt) in Python
f = open(
    "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/1.Intro to IO with Files/myFile.txt"
)

print(type(f.read()))  # file.read() returns a string

print(f.read())
print(f.read(5))  # 因為 上面的 read()seek 已經到了文字的最後面 所以在 read() 就會找不到文字

# 所以可以使用 seek 定義位置
print(f.read())
f.seek(0)
print(f.read())
