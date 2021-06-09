class bankaccount:
    def __init__(self, int_rate=0.01, balance=0):
       self.balance = balance
       self.int__rate = int_rate

    def deposit(self, amount):
        self.balance += amount



     def withdraw(self,amount):
         if amount <= self.balance:
             self.balance-= amount
             return True

else:
    print("Insufficient funds: charging a $5 fee")
    self.balance-= 5
    return False


 def display_account_info(self):
     print(f"balance: {self.balance}")




 def yield_interest(self):
     self.balance += self.int_rate * self.balance      





