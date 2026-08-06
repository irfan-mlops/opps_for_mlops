# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound...")


# Drived Class
class dog(Animal):

    def speak(self):
        print(f"{self.name} is barked..")


animal = Animal("German Shafart")
animal.speak()
    
dog1 = dog("small dog")
dog1.speak()