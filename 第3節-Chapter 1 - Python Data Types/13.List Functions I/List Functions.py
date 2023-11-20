# insert() - 插入的意思
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.insert(2, "Aaron")
print(friends)

# remove() - 移除某一個特定的 element
friends.remove("Nelson")
print(friends)
# 如果移除list裡面沒有的東西，會出現 valueError: list.remove(x): x not in list
# friends.remove("Benson")
# print(friends)

# clear() - 清空 list
friends.clear()
print(friends)

# sort() - 排序的意思 可以按照 字母大小寫 也是 資料中很重要的演算法
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.sort()
print(friends)

numbers = [4, -3, 6, 1, 3, 2]
numbers.sort()
print(numbers)

# reverse() - 反轉的意思
friends.reverse()
friends2 = friends[::-1]
print(friends)
print(friends2)
