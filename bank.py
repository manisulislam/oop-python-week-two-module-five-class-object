class Bank:
    

    def __init__(self, balance):
        self.balance= balance
        self.min_withdraw= 100
        self.max_withdraw= 5000000
    
    def get_balance(self):
        return self.balance
    
    def deposit_balance(self, amount):
        if amount> 0:
            self.balance+=amount
    
    def withdraw_balance(self, amount):
        if amount<self.min_withdraw:
            print(f"fokira . can not withdrow {self.min_withdraw}")
        elif amount> self.max_withdraw:
            print(f"bank fokir hoya jabe. can not withdraw {self.max_withdraw}")
        else:
            self.balance-=amount
            print(f"here is your money {amount}")
            print(f"current balance {self.balance}")
brac= Bank(30000)
brac.withdraw_balance(30)
brac.withdraw_balance(10000)