class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print (f"Employee name is : {self.name} and id is: {self.id}")
        
class Programmer(Employee):
    def skills(self):
        print("Python")        

e1 = Employee("Harshil",1)
e1.showDetails()

e2 = Programmer("Manoj",2)
e2.showDetails()