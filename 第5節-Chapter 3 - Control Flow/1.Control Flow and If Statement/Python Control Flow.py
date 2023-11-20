# if statement
if False:
    print("This is so true!!")
else:
    print("This is false.")

age = 15
if age < 8:
    print("Movie is free for you!!")
else:
    print("You need to pay $300!")

# <8 => free
# >=8 and <65 => 300
# >= 65 => half
age = 5
if age < 8:
    print("Movie is free for you!!")
elif 8 <= age < 65:
    print("You need to pay $300!")
else:
    print("You only need to pay $150")

# Truthy and Falsy
if (5 > 3) and []:
    print("the condition is trud")
else:
    print("the condition is false")

# 小習慣
k = True
if k == True:
    print("Variable k is true")
else:
    print("Variable k is false")
# 可以改成
if k:
    print("variable k is true")
