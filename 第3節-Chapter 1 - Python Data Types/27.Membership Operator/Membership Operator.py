#  1. in - 確認是否有在 string, lists tuples, dictionaries, sets 中
#  2. not in - 確認是沒有在 string, lists tuples, dictionaries, sets 中
a = "ABCD"
if "A" in a:
    print("A is in ", a)

# 如果不用 上面的方法 要如何寫?
myString = "Today is a good day. The weather in Hawaii is not bad."

isIn = False

for i in range(len(myString)):
    if "A" == myString[i]:
        isIn = True
print(isIn)
