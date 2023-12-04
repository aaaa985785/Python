# 5. Write a function called "swap" that takes a string as input, and returns a new string with lowercase changed to uppercase, uppercase changed to lowercase.
# swap("Aloha"); # returns "aLOHA"
# swap("Love you."); # returns "lOVE YOU."
def swap(string):
    result = ""
    for letter in string:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result


print(swap("Aloha"))
print(swap("Love you."))


# 6. Write a function called "findMin" which takes an list as input, and returns the minimum element in the input list.
# findMin([1, 2, 5, 6, 99, 4, 5]); # returns 1
# findMin([]); # returns undefined
# findMin([1, 6, 0, 33, 44, 88, -10]); # returns -10
# 邏輯
def findMin(lst):
    if len(lst) == 0:
        return "undefined"
    # set the index 0 element to be the min element
    min_element = lst[0]
    # for loop, in each interation
    for ele in lst:
        # if the element is less than my current min element
        if ele < min_element:
            min_element = ele


# if yes, then change my min element
    return min_element

print(findMin([1, 2, 5, 6, 99, 4, 5]))
print(findMin([]))
print(findMin([1, 6, 0, 33, 44, 88, -10]))
