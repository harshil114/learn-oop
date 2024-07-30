class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private attribute
    
    def reset_pass(self):
        print(self.__acc_pass) #can be use in same class

acc1 = Account(12345,"qwer")
print(acc1.acc_no)
# print(acc1.acc_pass) AttributeError: 'Account' object has no attribute 'acc_pass'
print(acc1.reset_pass())


class Person:
    __name: "any"
    
    def __hello(self): #private method
        print("Hello person")
    
    def welcome(self): #welcome method for using private method __hello
        self.__hello()
        
p1 = Person()
print(p1.welcome())