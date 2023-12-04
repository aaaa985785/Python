# 第一 先學 form sys import argv
# 用來得到 其他的資料 this is how we get command line arguments
# argv 是會將東西放在 [""] 裡面，例如 print(argv) 在命令字元 python try.py myFile.txt 得到 ['try.py', 'myFile.txt']
from sys import argv

# 第二 先判斷使用者有沒有給一個文件，就可以使用 argv 來判斷長度
if len(argv) < 2:
    print("Please provide a filename.")

# 第三 讀取文件的做法
else:
    file = open(argv[1])
    print(file
          )  # <_io.TextIOWrapper name='myFile.txt' mode='r' encoding='UTF-8'>
    lines = file.read()
    print(type(lines))  # str
    print(lines)  # 文件的內容

    # 第四 開始做 wc 的邏輯
    lines = lines.split("\n")
    print(
        lines
    )  # a list of strings ['roses are red', 'sky is blue', 'syntax error in line 32', '']

    word_count = 0
    letter_count = 0
    for line in lines:
        words = line.split(" ")
        word_count += len(words)  # 總共多少字
        letter_count += len(line)  # 總共多少字元
    print(f"The line count is {word_count}")
    print(f"The letter count is {letter_count}")

    line_count = len(lines) - 1  # 總共幾行
    print(f"The line count is {line_count}")
