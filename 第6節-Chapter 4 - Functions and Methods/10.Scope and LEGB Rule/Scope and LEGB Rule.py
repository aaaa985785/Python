# Scope 範圍
name = "Wilson"


def greet():
    name = "Grace"

    def hello():
        print("Hello, my name is " + name)

    def hello2():
        print("greeting from hello2.")
        hello()

    hello()
