# Default Arguments
def sum(n1, n2):
    return n1 + n2


print(sum(12, 25))

# 如果少打一個參數 TypeError: sum() missing 1 required positional argument: 'n2'
# print(sum(12))


# 如果要解決這個問題，python 有提供一個辦法 Default Arguments
def sums(n1, n2=0):
    return n1 + n2


print(sums(12))

# 但有個問題就是 不能這樣寫 SyntaxError: non-default argument follows default argument
# def sums(n1=10, n2):
#     return n1 + n2

print(sums(12))  # 因為這邊預設是抓第一個


# default argument
def sum(n1=0, n2=0):
    return n1 + n2


# keyword argument
print(sum(n2=100, n1=50))
