# string 加上 "" 就可以代表 字串，後面加上[] 就可以依照索引找到該字母
# 如果 超過 該字串的數字 就會顯示 string index out of range
print("hello"[1])

i = 4
print("hello"[i])

# 獲取想要的字母(slicing)
x = "abcdefg"
print(x[2:6])

# 使用 stepsize要走幾步
print(x[1:6:2])
print(x[::-1])

# 如果只要顯示偶數的值
print(x[::2])
