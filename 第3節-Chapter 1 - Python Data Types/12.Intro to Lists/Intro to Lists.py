# 通常有關連性的data的時候會使用 list
# 1 不好的使用
friend1 = "Mike"
friend2 = "Josh"
friend3 = "Jreey"
print(f"{friend1}, {friend2}, {friend3} are my friends.")

# 2 使用 list 做法
friendList = ["Mike", "Josh", "Jerry"]
print(f"{friendList[0]}, {friendList[1]}, {friendList[2]} are my friends.")

# len() - 長度
print(len(friendList))

# slicing rule (一樣可以像 string 切到想要的數字範圍)
luckyNumbers = [2, 3, 4, 5, 6, 7, 10]
print(luckyNumbers[0:3])
# 一樣想要偶數位可以這樣
print(luckyNumbers[::2])
# 將整個 list 倒過來
print(luckyNumbers[::-1])

# count() - 這個 list 某個 element(元素) 出現的次數
x = [1, 2, 1]
print(x.count(1))

# index() - 該 element 位置
print(x.index(1))

# list 也可以使用 + 來 concatenation(串接)
x = [1, 2, 1]
y = [3, 4, 5]
print(x + y)

# list 也可以與數字 相乘
x = [3, 3, 3]
print(x * 3)

# list is mutable(可以改變的)(Remember, strings are immutable)
x = [1, 2, 1]
x[1] = 10
print(x)
