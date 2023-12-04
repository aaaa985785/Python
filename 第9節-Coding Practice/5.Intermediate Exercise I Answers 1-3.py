# 1. Write a function called "mySort" that takes an list of integers as input, and returns the sorted version of the input list. You are not allowed to use the built-in sorted() function.
# mySort([17, 0, -3, 2, 1, 0.5]); # returns [-3, 0, 0.5, 1, 2, 17]
def findMin(lst):
    if len(lst) == 0:
        return "undefined"
    result = lst[0]
    for ele in lst:
        if ele < result:
            result = ele
    return result


def mySort(myList):
    result_list = []
    while len(myList) > 0:
        min_element = findMin(myList)
        result_list.append(min_element)
        myList.remove(min_element)
    return result_list


print(mySort([17, 0, -3, 2, 1, 0.5]))


# 2. Write a function called "isPrime" that takes an integer as input, and returns a boolean value that indicates if the input number is prime.
# isPrime(1); # returns false
# isPrime(5); # returns true
# isPrime(91); # returns false
# isPrime(1000000); # returns false
# prime?
# 例如 5 只有 1 跟 5 可以整除  這樣叫質數
def is_prime(n):
    if n == 1:
        return False

    starter = 2
    while starter < n:
        if n % starter == 0:
            print(starter)
            return False
        starter += 1
    return True


print(is_prime(1))
print(is_prime(5))
print(is_prime(91))
print(is_prime(1000000))

# 3. Write a function called "palindrome" that checks if the input string is a palindrome. (Search on google if you don't know what a palindrome is.)
# palindrome("bearaeb"); # true
# palindrome("Whatever revetahW"); # true
# palindrome("Aloha, how are you today?"); # false
# solution1
# beareab len(string) = 7
# 0123456
# i     len(string) - 1 - i
import math


def palindrome(string):
    # for loop
    for i in range(0, math.floor(len(string) / 2)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


print(palindrome("bearaeb"))
print(palindrome("Whatever revetahW"))
print(palindrome("Aloha, how are you today?"))


# solution2
# beareab
# left+=1     right-=1
# stop while loop when left is bigger than right
def palindrome2(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(palindrome2("bearaeb"))
print(palindrome2("Whatever revetahW"))
print(palindrome2("Aloha, how are you today?"))
