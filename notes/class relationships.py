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
    def __init__(self,radius):
        self.radius=radius

class Car:
    def __init__(self, make, model, hoarsepower, wheel_radius):
        self.make=make
        self.model=model
        self.Engine=Engine(hoarsepower)
        self.wheels=[Wheel(wheel_radius)for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.Engine.hoarsepower} {self.wheels[0].radius} {self.wheels[1].radius} {self.wheels[2].radius} {self.wheels[3].radius}"

car=Car(make='cat',model='Meow', hoarsepower=87, wheel_radius=3)

print(car.display_car())