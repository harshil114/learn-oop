class Student:
    clg_name = "ABC clg"        
    name = "any"
        
    def __init__(self,name,marks):
        self.name = name   
        self.marks = marks
    
    def welcome(self): 
        print("Welcome student")
        print("Welcome",self.name) 
        
s1 = Student("harshil",1)
s1.welcome()