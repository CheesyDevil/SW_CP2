#SW 2nd Classes notes

#example
class Dog:
    def __init__(self, name,breed, age):
        self.name=name.capitalize()
        self.breed=breed.title()
        self.age=age
    def __str__(self):
        return f"Name:{self.name}\nBreed:{self.breed} \nAge:{self.age}"
    def speak(self):
        return f'{self.name}: Bark'
doug=Dog("doug","Golden retriever", 3)
pongo=Dog("pongo","dalmation",8)

print(doug)
print(doug.speak())