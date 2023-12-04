# Deleting Files and Folders
import os

os.remove(
    "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/5.DeletingFiles and Folders/index.html"
)  # os unlink functionality 永久移除

os.rmdir(
    "C:/Users/aaaa9/Desktop/Python Codes/第10節-Chapter 5 - IO in Python/5.DeletingFiles and Folders/newFolder"
)

# 因為資料夾裡面有文件不能刪除，但如果還是想刪除有兩種方法
# 第一種 os.walk() to travel though the folder
# 第二種 shutil - shell(跟電腦核心交談的管道) utility
