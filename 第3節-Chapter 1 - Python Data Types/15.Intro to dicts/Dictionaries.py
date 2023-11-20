# Dictionaries 基本使用
person = {"name": "Wilson", "age": 25}
print(person["name"])

# what data types can be used for keys? 這個後面章節講
# what data types can be used for values? 任何都可以
person = {"x": {"age": [10, 20, 30]}}
print(person["x"]["age"][0])

# 最後講解 可以手動加入 物件的值
x = {}
x["name"] = "Grace"
x["age"] = 26
print(x)
