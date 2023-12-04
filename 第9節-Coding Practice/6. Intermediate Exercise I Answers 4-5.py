# 4. Write a function called "pyramid" that takes an integer as input, and prints a pyramid in the following pattern:
# pyramid(1);
# *
# pyramid(2);
#  *
# ***
# pyramid(4);
#    * 1
#   *** 3
#  ***** 5
# ******* 7 (3 + 1 + 3)
# the bottom layer has ( 2 * n - 1) stars
def pyramid(n):
    space = n - 1
    star = 1
    for i in range(n):
        print(space * " " + star * '*')
        star += 2
        space -= 1


pyramid(7)


# 5. Write a function called "inversePyramid" that draws pyramid upside down.
# inversePyramid(4);
# *******
#  *****
#   ***
#    *
# 第一種 有點偷吃步
def inverse_pyramid(m):
    result = []

    def pyramid(n):
        space = n - 1
        star = 1
        for i in range(n):
            result.append(space * ' ' + star * '*')
            star += 2
            space -= 1

    pyramid(m)
    result.reverse()
    for line in result:
        print(line)


inverse_pyramid(4)


# 第二種
# ******* 2n-1
#  *****
#   ***
#    *
def inverse_pyramid(n):
    stars = 2 * n - 1
    space = 0
    for i in range(n):
        print(space * ' ' + stars * '*')
        stars -= 2
        space += 1


inverse_pyramid(4)
