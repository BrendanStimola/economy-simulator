class Bank:
    def __init__(self):

        self.name = "Main Bank"

        self.deposits = 0

        self.loans = 0

        self.reserves = 100

        self.loan_interest_rate = 0.05

        self.deposit_interest_rate = 0.02

        self.interest_income = 0

        self.deposit_interest = 0

        self.number_of_loans = 0

        self.maximum_loan = 100

        self.defaulted_loans = 0

        self.loan_losses = 0

        self.minimum_capital_ratio = 0.08

        self.minimum_liquidity_ratio = 0.10

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
        if borrower.loan + amount > borrower.maximum_debt:
            print("too much debt")
            return False

        interest_rate = self.get_loan_interest_rate(borrower)

        if interest_rate is None:
            return False
        future_capital_ratio = self.projected_capital_ratio(amount)
        if future_capital_ratio < self.minimum_capital_ratio:
            print(f"capital ratio too low: {future_capital_ratio}")
            return False

        borrower.money += amount

        borrower.loan += amount

        borrower.loan_interest_rate = interest_rate

        self.loans += amount

        self.deposits += amount

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

        if borrower.money <= 100:
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
        if amount > self.maximum_loan:
            return False
        if amount > self.reserves:
            return False
        if borrower.loan + amount > borrower.maximum_debt:
            return False
        interest_rate = self.get_loan_interest_rate(borrower)
        if interest_rate is None:
            return False
        projected_ratio = self.projected_capital_ratio(amount)
        if projected_ratio < self.minimum_capital_ratio:
            return False
        return True

    def process_loan_payments(self, borrower):
        if borrower.loan <= 0:
            return True
        interest = (borrower.loan * borrower.loan_interest_rate)/365

        if borrower.money >= interest:

            borrower.money -= interest

            self.reserves += interest

            self.interest_income += interest

            return True
        else:
            self.default_loan(borrower)
            return False

    def default_loan(self, borrower):

        loan_amount = borrower.loan

        self.defaulted_loans += 1

        self.loan_losses += loan_amount

        self.loans -= loan_amount

        self.reserves -= loan_amount

        borrower.loan = 0

        borrower.loan_interest_rate = 0

        return loan_amount
    
    def total_assets(self):
        return self.reserves + self.loans

    def total_liabilities(self):
        return self.deposits

    def calculate_capital(self):
        return self.total_assets() - self.total_liabilities()

    def capital_ratio(self):

        assets = self.total_assets()

        if assets <= 0:
            return 0
        if self.calculate_capital() <= 0:
            return 0

        return self.calculate_capital()/assets

    def liquidity_ratio(self):

        if self.deposits <= 0:
            return 0
        return self.reserves/self.deposits

    def projected_capital_ratio(self, amount):
        projected_assets = self.total_assets() + amount

        if projected_assets <= 0:
            return 0

        capital = self.calculate_capital()

        return capital / projected_assets