#  1. difference() - A{1,3,4,5}、B{3,4,7,8}兩個集合交集(intersection)的內容為A∩B={3,4}，當 A-B={1,5}、B-A{7,8}這樣就是 difference()
#  2. intersection() - 兩個集合交集 A∩B={3,4}
#  6. union() - 連集 A⋃B={1,3,4,5,7,8,9}
a = set({1, 3, 4, 5})  # 也可以寫 a = {1, 3, 4, 5}
b = {3, 4, 7, 8}
print(a.difference(b))  # A - B
print(b.difference(a))  # B - A
print(a.intersection(b))
print(b.intersection(a))
print(a.union(b))
print(b.union(a))

#  3. isdisjoint() - 判斷兩個集合是否有相交 A∩B=∅(空集合)
#  4. issubset() - 子集合 A⊆B A是B的子集合
#  5. issuperset() - 母集合
a = {1, 3, 4, 5}
b = {3, 4, 7, 8}

print(a.isdisjoint(b))
print(a.issuperset(b))
print(a.issubset(b))
