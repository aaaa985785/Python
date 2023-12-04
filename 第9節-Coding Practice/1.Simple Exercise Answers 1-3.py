# 1. Write a function called "printMany" that prints out integers 1, 2, 3, ...., 100
# printMany();
# 1
# 2
# ...
# 100
def printMany():
    for i in range(1, 101):
        print(i)


printMany()


# 2. Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.
# printEvery3();
# 1
# 4
# ...
# 88
def printEvery3():
    for i in range(1, 89, 3):
        print(i)


printEvery3()


# 3. Write a function celled "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.
# position("abcd") returns -1
# position("AbcD") returns ('A', 0)
# position("abCD") returns ('C', 2)
def position(string):
    # enumerate function
    for num, s in enumerate(string):
        if s == s.upper():
            return (s, num)
    return -1


print(position("abcd"))
print(position("AbcD"))
print(position("abCD"))


# 4.如果我們希望找到「最後一個大寫字母與其索引位置」，要怎麼做呢？
# 第一種是「反向」的運作迴圈
def position(string):
    for index in range(len(string) - 1, -1, -1):
        if string[index] == string[index].upper():
            return (string[index], index)
    return -1


print(position("abCD"))


# 另一種作法是，用一個變數裝載「目前」滿足條件的值。只要發現新滿足條件的值，就取代這個變數內的數值
def position(string):
    final_answer = -1
    for num, s in enumerate(string):
        if s == s.upper():
            final_answer = (s, num)
    return final_answer


print(position("abCD"))
