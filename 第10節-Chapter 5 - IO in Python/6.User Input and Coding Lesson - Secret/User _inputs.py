# User Inputs
# user_input = input("How old are you?")
# user_address = input("Where do you live?")
# print("---------------------------------")
# print(user_input)
# print(type(user_input))

# ❗ Coding Lesson - Secret(終極密碼)
# 1 - 100
import random

secret = random.randint(1, 100)  # generate a random integer from 1 to 100
min_value = 1
max_value = 100

while True:
    guess = input(f"Make your guess between {min_value} and {max_value}: ")
    if int(guess) < min_value or int(guess) > max_value:
        print("Your guess is not within the range!!")
        continue

    if int(guess) == secret:
        print(f"The secret is {secret}")
        break
    elif int(guess) < secret:
        min_value = int(guess)
    elif int(guess) > secret:
        max_value = int(guess)
