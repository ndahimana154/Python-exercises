class BankAccount:
    def  __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number;
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit (self):
        return (f"{self.customer_name} You are depositing")
    def withdraw(self):
        return "You are withdrawing"
        
account1 = BankAccount(1000032,300,"12.01.2023","Kwizera")

print(account1.deposit())