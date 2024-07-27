class Student:
    
    #default constructor
    # def __init__(self):
    #     # print("this will called without calling it")
    #     pass
    
    #parametrized constructors 
    def __init__(self,name,marks):        
        self.name = name
        self.marks = marks   
    
s1 = Student("harshil soni",56)
print(s1.name)
print(s1.marks)

s2 = Student("Harshil Vispute",65)
print(s2.name)
print(s2.marks)