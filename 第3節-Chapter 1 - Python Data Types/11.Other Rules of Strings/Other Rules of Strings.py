# Immutability(不可改變的) 雖然不能改變的規則，但是可以用 slicing 加上 + 修改原來的字串
name = "Sam donaldson"  #想改名成 Pam Donaldson
name = 'P' + name[1:]
print(name)

# String multiplied(相乘) by numbers is a valid(有效) poeration(運算)! 數字只能整數，而且只能乘數字
print("Wilson" * 10)
print("A" * 5)

# we can use the format method and f-string
