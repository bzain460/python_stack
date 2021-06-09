class User:
    def __init__(self):
        self.name = "client"
        self.account_balance = 0
        self.amount = 0       

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
    def make_deposit(self, amount):
            self.account_balance += amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount) 
        other_user.make_deposit(amount)
     

user1 = User()
user1.make_deposit(150)
user1.make_deposit(200)
user1.make_deposit(1000)
user1.make_withdrawal(150)
user1.display_user_balance()

user2 = User()
user2.name = "Ahmad"
user2.make_deposit(50)
user2.make_deposit(120)
user2.make_withdrawal(250)
user2.make_withdrawal(400)
user2.display_user_balance()

user3 = User()
user3.name = "Muna"
user3.make_deposit(1400)
user3.make_withdrawal(400)
user3.make_withdrawal(130)
user3.make_withdrawal(700)
user3.display_user_balance()

print("After transfer:")
user1.transfer_money(user3,200)
user1.display_user_balance()
user3.display_user_balance()