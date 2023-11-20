# abs()
print(abs(-5))  # 5
print(abs(5))  # 5

# pow()
print(pow(2, 10))  # 1024

# min()
print(min(4, 2, 1, -10, 100, -7))
print(max(4, 2, 1, -10, 100, -7, 1000))

# round()
print(round(2.6))
#❗但有個奇怪的地方，當如果處理到，什麼.5的時候，如果四捨五入的結果為基數，就不會進位
print(round(2.5))  # 照理說應該是 3
print(round(3.5))  # 照理說應該是 4
print(round(6.5))
print(round(5.5))

# int()
print(int(3.0))

# float()
print(float(3.0))

# str()
print(str(3) + str(3))

# 當要使用 Math Module 要使用 import
import math

# e
print(math.e)

# pi
print(math.pi)

# floor()
print(math.floor(4.999))

# ceil()
print(math.ceil(4.00000001))

# sqrt()
print(math.sqrt(36))
