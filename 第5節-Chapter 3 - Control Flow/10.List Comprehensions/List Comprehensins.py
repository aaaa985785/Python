# Comprehension
# 之所以會有這的出現是因為 很常做下面的事情 就是將 list 給他開平方
x = [1, 2, 3, 4]
squared_x = []
for item in x:
    squared_x.append(item**2)
print(squared_x)

# 因為太常出現了以上的例子，所以就出現 Comprehension 來簡化寫法
x = [2, 4, 6, 8]
squared_y = [item**2 for item in x if item >= 3]
print(squared_y)

# Dictionary 使用
x = [1, 2, 3, 4]
x_squated_dict = {item: item**2 for item in x if item > 2}
print(x_squated_dict)

# set 使用
x = [1, 2, 3, 4]
x_squated_set = {item**2 for item in x if item > 2}
print(x_squated_set)

# Generator 使用
x = [1, 2, 3, 4]
x_squated_generator = (item**2 for item in x)

for i in x_squated_generator:
    print(i)
