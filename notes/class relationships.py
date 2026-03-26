class Animal:
    def __init__(self):
        pass
class Dog(Animal):
    pass

class Library:
    def __init__(self, name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

class Book:
    def __init__(self, author, title):
        self.author=author
        self.title=title


library=Library("NYPL")
book1=Book("Cat","meow")
book2=Book("Dog","Woof")
book3=Book("Fox","Ding-Ding-Ding")


class Engine:
    def __init__(self,hoarsepower):
        self.hoarsepower=hoarsepower

class Wheel:
    def __init__(self,radius,cap):
        self.radius=radius
        self.cap=cap
    def __str__(self):
        return f"{self.radius}"

class Car:
    def __init__(self, make, model, hoarsepower, wheel_radius, wheel_cap):
        self.make=make
        self.model=model
        self.Engine=Engine(hoarsepower)
        self.wheels=[Wheel(wheel_radius,wheel_cap)for wheel in range(4)]
    def p_wheel(self):
        string=""
        for i in self.wheels:
            string=f"{string}{i.cap}\n"
        print(string)

    def display_car(self):
        return f"{self.make} {self.model} {self.Engine.hoarsepower} {self.wheels[0].radius} {self.wheels[1].radius} {self.wheels[2].radius} {self.wheels[3].radius}"

car=Car(make='cat',model='Meow', hoarsepower=87, wheel_radius=3, wheel_cap=4)
car.p_wheel()
print(car.display_car())