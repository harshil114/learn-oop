#create account class with 2 attributes - balance and acc no
# create methods for debit, credit and printing the balance

class Account:
    
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs." ,amount, "was debited")
        print("Total balance: ",self.get_balance())
        
    def credit(self,amount):
        self.balance += amount
        print("Rs." ,amount ,"was credited")
        print("Total balance: ",self.get_balance())
    
    def get_balance(self):
        return self.balance        
    
acc1 = Account(2000,123456)
print("Initial account balance: ",acc1.balance)

acc1.credit(2000)
acc1.debit(1000)
        
        
    
    