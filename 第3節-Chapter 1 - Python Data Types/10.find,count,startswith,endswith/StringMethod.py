# count() - 數的意思，出現幾次
string = "Good Today is a good day."
print(string.count("a"))
print(string.count("good"))

# 因為 count 只會抓取你輸入的 不會自動都抓大小寫，所以你想要大小寫都要抓的話，可以先把原來字串轉成小寫 再抓取
print(string.lower().count("good"))

# find() - 跟前面章節講的 index() 一樣，都可以找到 substring 的位置，但跟 index() 不一樣的地方 index 如果輸入字串沒有的值會報錯，而 find() 會回傳 -1
print(string.find("day"))
print(string.find("apple"))
# print(string.index("apple"))

# startswith() - 判斷開頭是否正確，回傳 true or false
name = "Wilson"
print(name.startswith("W"))
