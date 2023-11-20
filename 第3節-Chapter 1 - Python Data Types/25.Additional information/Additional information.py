# nj
x = 3 + 4j
y = 5 - 7j
print(x + y)


# None
def hello():  # hello is stored in RAM (function 會被放入 RAM)
    print("hello")


print(hello)  # 會出現 hello at 0x000001B.. 之類的 因為沒有加上 () 所以是指 要顯示 RAM 位置
print(
    hello()
)  # 會出現 hello None 之所以會出現 None 是因為 function 會 return 值 ，因為 hello() 沒有設定 return 的值

# 0.1+0.2-0.3?
print(0.1 + 0.2 - 0.3)

# join()
myList = ["a", "b", "c", "d"]
myString = "|".join(myList)
print(myString)
