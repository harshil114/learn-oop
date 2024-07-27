class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Harshil")
print(s1) #print object
del s1 #deleting s1 obj
print (s1) #NameError: name 's1' is not defined