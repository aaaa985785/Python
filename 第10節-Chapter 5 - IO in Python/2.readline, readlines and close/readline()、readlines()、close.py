# readlines()
f = open(
    "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/1.Intro to IO with Files/myFile.txt"
)
print(f.readlines())

for line in f.readlines():
    print(line)

# readline() 讀取行數內容
print(f.readline())

# 如果不知道文件幾行又怕使用 readlines() 記憶體被塞滿 可以使用這樣
while True:
    line = f.readline()
    if not line:
        break
    else:
        print(line)

# close()
f.close()
