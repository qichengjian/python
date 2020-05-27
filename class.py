class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")


    def draw(self):
        print(f"draw {self.x}")


class P:
    def draw(self):
        print("draw")


point1 = P()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point(10,20)
print(point2.x)
point2.draw()
print(point2.y)



class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


dog = Dog();
dog.walk()
dog.bark()

###类的定义 class 继承， pass避免空类警告