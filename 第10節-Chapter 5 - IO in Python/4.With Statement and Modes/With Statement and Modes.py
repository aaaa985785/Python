# With statement
with open(
        "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/1.Intro to IO with Files/myFile.txt"
) as my_file:  #variable
    all_content = my_file.read()
    print(all_content)

# 1. "r" - Read
with open(
        "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/1.Intro to IO with Files/myFile.txt",
        mode="r") as my_file:  #variable
    all_content = my_file.read()
    print(all_content)

# 2. "a" - Append
with open(
        "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/1.Intro to IO with Files/myFile.txt",
        mode="a") as my_file:  #variable
    my_file.write("Learning python is so fun.")

# 3. "w" - Write 整個覆蓋掉
with open(
        "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/1.Intro to IO with Files/myFile.txt",
        mode="w") as my_file:  #variable
    my_file.write(
        "Learning python is so fun.\nLearning JavaScript is so fun as well.\n")

# 4. "x" - Create
