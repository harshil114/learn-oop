class Car:
    def __init__(self,type):
        self.type = type
        
class Sedan(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
    
car1 = Sedan("Ciaz","Sedan")
print(car1.name)
print(car1.type)
       