# replace() - 替代
name = "Josh Jordan"
print(name.replace("J", "K"))
print(name.replace("Josh", "kyle"))

# split() - 將字串變成陣列(list)，依據split()中的條件去區分形成陣列
sentence = "Today is a good day."
print(sentence.split(" "))

# list() 是 typecasting - 將字串變成陣列(list)，character by character(每個字一個一個分開形成陣列，包含空白建)
print(list(sentence))

# format() - fstring概念，前面有講到不同的資料型態不能使用加減之類的，但是資料型態很多沒辦法記得那麼多轉換的資料，所以有了 format(), fstring
# 1
sentence = "I have a string {}".format("here it is")
sentences = "I have a string {}".format(15)
print(sentence + "," + sentences)

# 2
print("{}, {}, {}".format(20, "here is another string", 3.14))

# 3
print("{0}, {0}, {0}".format(20, "here is another string", 3.14))

# 4
print("{name}, {address}, {age}".format(name="Wilson",
                                        age=25,
                                        address="Hawaii"))

# fstring - Python 3.6 出現的 目的就是要讓 format() 的效果 更好用
myName = "Wilson"
age = 25
print(f"Hello, my name is {myName}, I am {age} years old.")
