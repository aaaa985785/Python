# OOP
my_list = [1, 2, 3, 4]
print(type(my_list))


# class
class Robot:
    pass


my_robot = Robot()
print(my_robot)


# __init__()  self是指自己
class Robot():
    # in classes, we can also define doctring
    """Robot class is for creating robots"""

    # contructor
    def __init__(self, inputname, inputage):
        self.name = inputname
        self.age = inputage

    def walk(self):
        print(f"{self.name} is walking...")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours.")


my_robot_1 = Robot("Wilson", 25)
my_robot_2 = Robot("Grace", 26)
print(my_robot_1.name)
print(my_robot_1.age)
print(my_robot_1.__doc__)
my_robot_1.walk()
my_robot_1.sleep(15)
my_robot_2.walk()

print(my_robot_1.age < my_robot_2.age)
