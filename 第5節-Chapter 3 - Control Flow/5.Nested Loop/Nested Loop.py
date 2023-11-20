# Nested Loops

# 驗證執行幾次
counter = 0

# 4 x 7 = 28
for i in "1234":
    for j in "abcdefg":
        print(i, j)
        counter += 1

print(f"counter is now {counter}")
