class Bank:
    def __init__(self):

        self.name = "Main Bank"

        self.deposits = 0

        self.loans = 0

        self.reserves = 0

        self.loan_interest_rate = 0.05

        self.deposit_interest_rate = 0.02

        self.interest_income = 0

        self.deposit_interest = 0

        self.number_of_loans = 0

    def deposit(self, customer, amount):
        if amount < 0:
            return False
        if customer.money < amount:
            return False
        
        customer.money -= amount

        customer.deposit += amount

        self.deposits += amount

        self.reserves += amount

        return True

    def pay_deposit_interest(self, customer):

        if customer.deposit <= 0:
            return False

        interest = (customer.deposit * self.deposit_interest_rate/365)

        customer.deposit += interest

        self.reserves -= interest

        self.deposit_interest += interest

        return interest

    def withdraw(self, customer, amount):
        if amount <= 0:
            return False
        if customer.deposit < amount:
            return False
        if self.reserves < amount:
            return False

        customer.money += amount

        customer.deposit -= amount

        self.deposits -= amount

        self.reserves -= amount

        return True
    
    def lend(self, borrower, amount):

        if amount <= 0:
            return False
        if amount > self.reserves:
            return False
        
        self.reserves -= amount

        borrower.money += amount

        borrower.loan = getattr(borrower, "loan", 0)+amount

        self.loans += amount

        self.number_of_loans += 1

        return True

    def collect_interest(self, borrower):
        if borrower.loan <= 0:
            return 0
        
        interest = (borrower.loan * self.loan_interest_rate)

        if borrower.money < interest:
            return 0

        borrower.money -= interest

        self.reserves += interest

        self.interest_income += interest

        return interest

    def repay_loan(self, borrower, amount):
        if amount <= 0:
            return False
        
        if borrower.loan <= 0:
            return False

        repayment = min(amount, borrower.loan)

        if borrower.money < repayment:
            return False

        borrower.money -= repayment

        borrower.loan -= repayment

        self.loans -= repayment

        self.reserves += repayment

        return True