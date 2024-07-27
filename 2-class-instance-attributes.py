class Student:
    clg_name = "ABC clg"    #class attribute which is same for all the obj which is store only once in memory
    name = "any"    #class attr
    
    def __init__(self,name,marks):
        self.name = name    #obj attr > class attr will print only this    #instace attribute which is not same for all the obj
        self.marks = marks  
    
    
s1 = Student("harshil soni",56)
print(s1.name)
# print(s1.marks)

# print(s1.clg_name)
print(Student.clg_name) #accessing with class name
