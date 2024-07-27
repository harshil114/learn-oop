class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("avg : ",sum/3)
        
s1 = Student("harshil",[22,30,34])
s1.get_avg()