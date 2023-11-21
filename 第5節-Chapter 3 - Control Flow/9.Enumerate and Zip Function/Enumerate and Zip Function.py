# Enumerate
# 使用計數器 讓只要獲取指定的字串
counter = 0
for letter in "How are you today?":
    if counter < 10:
        print(letter)
    counter += 1

# 上面方法有點複雜 所以就可以使用 Enumerate
for couter, char in enumerate("How are you today?"):
    if couter < 10:
        print(char)

# Zip Function
x = [1, 2, 3]
y = ['A', 'B', 'C']

for tuple in zip(x, y):
    print(tuple)
