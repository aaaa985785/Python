# pass
for i in "How are you?":
    # 因為 for 下面一定要寫東西，但是我不想寫 這時候就可以使用 pass
    pass
    # some codes go here
    print("hello")

# pass if
if True:
    pass
else:
    print("hello")


# pass function
def hello():
    pass


# break
print("Before the for loop")

for i in "123456789":
    if i == "5":
        break
    else:
        print(i)

print("After the for loop")

# break nested loop
for i in "123456789":
    for j in "abcdefg":
        if j == "c":
            break
        print(i, j)

# continue
for i in "ABCDE":
    if i == "B":
        continue
    print(i)

for i in "ABCDE":
    print("NOW the current i is " + i)
    continue
    print("Here is the line after continue")
