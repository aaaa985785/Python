# 在講 set 前，要來講一個很有趣的 tuple
# if an element in a tuple is mutable, then we can just select the element, and then change it
# if we want to use a tuple as a dictionary key, then all elements in the tuple has to be immutable

a = ([1, 2, 3], "Wilson")
# 這樣是不行的
# a[0] = "Grace"
# print(a)
# 但是這樣是可以的
a[0][1] = 100
print(a)

# 綜合練習 判斷可不可以當 dictionary key
# 1. 15                                     可以
# 2. 'Bob'                                  可以
# 3. ("Tom", [14, 23, 27])                  不行
# 4. ["filename", (15, 16)]                 不行
# 5. "filename"                             可以
# 6. ("filename", 25, "extension")          可以
