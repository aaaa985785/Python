# return
def myAddition(a, b):
    print(a + b)


def myAddition2(a, b):
    return a + b


myAddition(myAddition(10, 18), myAddition(25, 19))  # 可以這樣做 但是如果條件很多 就不建議這樣使用
print(
    myAddition(25, 10) + myAddition(88, 99)
)  # 這是會出現錯誤，因為該 funciton 是 NoneType 這樣是不能相加，這樣就需要 return 讓 function 變成有 Type
print(myAddition2(25, 10) + myAddition2(88, 99))

# 也可以這樣
result1 = myAddition2(10, 18)
result2 = myAddition2(26, 19)
result3 = myAddition2(15, 17)

print(result1 + result2 + result3)

# evaluate 在cmd中輸入python 直接 enter 這是 python sandbox


# return 會停止 下面的程式碼
def apple(a, b):
    result = a + b
    return result
    print(result)


# 在迴圈中也是遇到 ruturn 就會停止
def ssd(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 4:
                return
            print(i, j)


ssd(10, 15)
