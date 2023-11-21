# 一個問題 以下的方式 如果要 1~100 要怎麼辦
for i in "123456789":
    print(i)

# 因為要解決上面的問題，所以有了 range()
print(range(100))  # returns iterable object
for i in range(5):
    print(i)

# 看到 range() 裡面的數字 typecasting to list
# 不建議下列作法
mylist = list(range(0, 15, 2))
print(mylist)
# 推薦下列做法
