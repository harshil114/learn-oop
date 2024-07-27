class Car:
    
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True 
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()

#so here in start() we are giving procees for starting the car which is hided from the user who is starting the car through the obj car1. so this is abstraction.