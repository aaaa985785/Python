# 4. Write a function called "findSmallCount" that takes one list of integers and one integer as
#     input, and returns an integer indicating how many elements in the list is smaller than the input integer
# findSmallCount([1, 2, 3], 2) returns 1
# findSmallCount([1, 2, 3, 4, 5], 0) returns 0
def findSmallCount(lst, num):
    counter = 0
    for ele in lst:
        if ele < num:
            counter += 1
    return counter


print(findSmallCount([1, 2, 3], 2))
print(findSmallCount([1, 2, 3, 4, 5], 0))
print(findSmallCount([1, 2, 3, 4, 5], 100))


# 5. Write a function called "findSmallerTotal" that takes one list of integers and integer as
#     input, and returns the sum of all elements in the list that are smaller than the input integer.
# findSmallerTotal([1, 2, 3], 3) return 3
# findSmallerTotal([1, 2, 3], 1) return 0
# findSmallerTotal([3, 2, 5, 8, 7], 999) return 25
# findSmallerTotal([3, 2, 5, 8, 7], 0) return 0
def findSmallerTotal(lst, num):
    result = 0
    for ele in lst:
        if ele < num:
            result += ele
    return result


print(findSmallerTotal([1, 2, 3], 3))
print(findSmallerTotal([1, 2, 3], 1))
print(findSmallerTotal([3, 2, 5, 8, 7], 999))
print(findSmallerTotal([3, 2, 5, 8, 7], 0))


# 6. Write a function alled "findAllSmall" that takes one list of integers and another integer as
#     input, and returns an list of integers that contains all elements that are smaller than that input integer.
# findAllSmall([1, 2, 3], 10) returns [1, 2, 3]
# findAllSmall([1, 2, 3], 2) returns [1]
# findAllSmall([1, 3, 5, 4, 2], 4) returns [1, 3, 2]
def findAllSmall(lst, num):
    result = []
    for ele in lst:
        if ele < num:
            result.append(ele)
    return result


print(findAllSmall([1, 2, 3], 10))
print(findAllSmall([1, 2, 3], 2))
print(findAllSmall([1, 3, 5, 4, 2], 4))


# 7. Write a function called "summ" that takes one list of numbers, and return that sum of all
#     elements in the input list
# summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) returns 55
# summ([]) return 0
# summ([-10, -20, -30]) return -60
def summ(lst):
    result = 0
    for ele in lst:
        result += ele
    return result


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(summ([]))
print(summ([-10, -20, -30]))
