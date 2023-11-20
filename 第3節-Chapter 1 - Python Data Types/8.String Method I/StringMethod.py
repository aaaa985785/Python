# ln() - length 長度多少
print(len("Aloha"))

# int() 只能放 base 10(十進位) 的數字，不然會顯示 valuError: invalid literal for int() with base 10 : 'two hundred'
print(int("10"))

# upper()- 轉換成大寫 要注意的是 他是屬於 object-oriented programming(在python裡面所有的資料都是 物件 ，像是一台車裡面有很多性質，也可以做到很多動作，所以被稱為物件導向)
# 所以他不像前面章節那樣是使用 function 將值放入，而是使用物件 .upper() 來將物件轉換成大寫
name = "Wilson"
print(name.upper())

# isupper() - 檢查字串裡面是否都是大寫
name = "Wilson"
print(name.islower())

# 可以使用 method chaining
print(name.upper().isupper())

# index() - 在字串內找到要的字的位置
name = "Apple"
print(name.index("l"))
print(name.index("pp"))
print(name.index("ser"))  # substring(sub是子的意思) not found
