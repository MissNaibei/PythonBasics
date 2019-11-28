class Atmcard():
    bank = "standardChartered"
    pin = 0
    balance = 0

    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def setpin(self):
        if self.pin == "KIS" :
            return("Login Successful!")
        else:
            return("Access Denied. You have exceeded your maximum attempts.")

    def checkBalance(self):
        return self.balance

    def withdraw(self,m):
        # self.balance+=m
        self.balance = self.balance-m
        if m > self.balance:
            return("Insufficient funds!")

    def cashDeposit (self, m):
        # self.balance+=m
        self.balance = self.balance + m
        return("Deposit successful. See you again!")



atm1 = Atmcard("KIS", 5000)
print(atm1.setpin())
print(atm1.checkBalance())
print(atm1.withdraw(1200))
print(atm1.cashDeposit(10023))
print(atm1.checkBalance())




