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

        self.maximum_loan = 100

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

        interest_rate = self.get_loan_interest_rate(borrower)
        
        self.reserves -= amount

        borrower.money += amount

        borrower.loan += amount

        borrower.loan_interest_rate = interest_rate

        self.loans += amount

        self.number_of_loans += 1

        return True

    def collect_interest(self, borrower):
        if borrower.loan <= 0:
            return 0
        
        interest = (borrower.loan * borrower.loan_interest_rate)

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

    def credit_score(self, borrower):

        score = 100

        if borrower.loan > borrower.money:
            score -= 30
        if borrower.profit < 0:
            score -= 30
        if borrower.loan > borrower.maximum_debt * 0.75:
            score -= 20
        return score

    def get_loan_interest_rate(self, borrower):
        score = self.credit_score(borrower)
        if score >= 80:
            return 0.05
        elif score >= 60:
            return 0.07
        elif score >= 50:
            return 0.1
        else:
            return None

    def assess_credit(self, borrower, amount):
        if amount <= 0:
            return False
        if amount >= self.maximum_loan:
            return False
        if amount > self.reserves:
            return False
        if borrower.loan + amount > borrower.maximum_debt:
            return False
        interest_rate = self.get_loan_interest_rate(borrower)
        if interest_rate is None:
            return False
        return True
