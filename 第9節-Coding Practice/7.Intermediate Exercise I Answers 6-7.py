# 6. Given a list of ints, return True if the list contains a 3 next to a 3.
# print(has_33([1, 5, 7, 3, 3])) # True
# print(has_33([])) # False
# print(has_33([4, 3, 2, 1, 0])) # False
def has_33(lst):
    result = False
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            result = True
    return result


print(has_33([1, 5, 7, 3, 3]))
print(has_33([]))
print(has_33([4, 3, 2, 1, 0]))


# 7. Write a function that check if a list contains a subsequence(裡面藏著007的數字不需要並排但是順序要正確) of 007
# print(spyGame([1, 2, 4, 0, 3, 0, 7])) # True
# print(spyGame([1, 2, 5, 0, 3, 1, 7])) # False
def spyGame(lst):
    string = "007"
    pointer_for_lst = 0
    pointer_for_string = 0
    while pointer_for_lst < len(lst):
        if lst[pointer_for_lst] == int(string[pointer_for_string]):
            pointer_for_string += 1
            if pointer_for_string == len(string):
                return True
        pointer_for_lst += 1
    return False


print(spyGame([1, 2, 4, 0, 3, 0, 7]))
print(spyGame([1, 2, 5, 0, 3, 1, 7]))
