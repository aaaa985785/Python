# append() - 將東西加入list
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.append("Aaron")
friends.append("Milly")
friends.append(15.0)
print(friends)

# pop() - 將 list 最後面的 emelemt 移除
friends.pop()
print(friends)
# pop 是會回傳被刪除的值 可以放在變數中
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
my_lost_friend = friends.pop()
print(friends)
print(my_lost_friend)

# copy() - list 是 copy by reference 但我只想要 copy by value 那這樣就可以使用此 Methods
# 1.先講觀念，以下面的例子來說，結果 y 會改變到 x 的值
x = [1, 2, 3, 4, 5, 6]
y = x
y[0] = 15
print(x)
print(y)
# 但是如果用以下的例子來看，結果有不一樣
a = 10
b = a
b = 15
print(a)
print(b)

# 2.正式使用
x = [1, 2, 3, 4, 5, 6]
y = x.copy()
y[0] = 15
print(x)
print(y)

# List of Lists
x = [1, 2, [4, 5, 6], 2, 1, [4, 3, [-10, 4]]]
print(x[2][1])

# List 抓到最後一個的方法
x = [1, 2, 3, 4, -2, -4, 5, 6, 7, 8, 9, 10]
print(x[11])
print(x[-1])
print(x[len(x) - 1])
