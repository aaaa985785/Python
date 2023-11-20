# 基本的 Set
mySet = set({1, 2, 3})
print(mySet)

# 將 list 轉換成 set
myList = [1, 4, 3, 2, 5, 1, 5]
mySet = set(myList)
print(mySet)

s = set()
#  1. add() - 新增元素
s.add(1)
s.add(2)
s.add(2)
s.add(3)

print(s)

#  2. clear() - 清空
s.clear()

#  3. copy() - 跟前面章節一樣

#  4. discaard() - 移除元素
s.discard(1)
print(s)
