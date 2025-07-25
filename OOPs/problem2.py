class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total Balance: ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total Balance: ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 3604972158)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)
acc1.debit(10000)
        