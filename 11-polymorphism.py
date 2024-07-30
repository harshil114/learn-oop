class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
    
animal1 = Dog()
animal2 = Cat()
print(animal1.sound())   
print(animal2.sound())   
    
