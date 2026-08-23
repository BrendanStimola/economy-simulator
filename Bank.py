class Bank:
    def __init__(self):
        self.name = "Main Bank"

        # Balance sheet
        self.deposits = 0.0
        self.loans = 0.0
        self.reserves = 100.0

        # Interest rates
        self.loan_interest_rate = 0.05
        self.deposit_interest_rate = 0.02

        # Income
        self.interest_income = 0.0
        self.deposit_interest = 0.0

        # Loans
        self.number_of_loans = 0
        self.maximum_loan = 100.0
        self.defaulted_loans = 0
        self.loan_losses = 0.0

        # Regulations
        self.minimum_capital_ratio = 0.08
        self.minimum_liquidity_ratio = 0.10

    def deposit(self, customer, amount):
        if amount <= 0:
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
            return 0.0

        interest = (
            customer.deposit
            * self.deposit_interest_rate
            / 365
        )

        customer.deposit += interest
        customer.interest_income += interest

        self.deposits += interest
        self.reserves -= interest
        self.deposit_interest += interest

        return interest

    def withdraw(self, customer, amount):
        if amount <= 0:
            return False

        amount = min(amount, customer.deposit)

        if amount <= 0:
            return False

        if self.reserves < amount:
            return False

        customer.deposit -= amount
        customer.money += amount

        self.deposits -= amount
        self.reserves -= amount

        return True

    def lend(self, borrower, amount):
        if not self.assess_credit(borrower, amount):
            return False

        interest_rate = self.get_loan_interest_rate(borrower)

        borrower.money += amount
        borrower.loan += amount
        borrower.loan_interest_rate = interest_rate

        self.loans += amount

        # Loan-created deposit/money.
        self.deposits += amount

        self.number_of_loans += 1

        return True

    def collect_interest(self, borrower):
        return self.process_loan_payments(borrower)

    def process_loan_payments(self, borrower):
        if borrower.loan <= 0:
            return True

        interest = (
            borrower.loan
            * borrower.loan_interest_rate
            / 365
        )

        if borrower.money >= interest:
            borrower.money -= interest

            self.reserves += interest
            self.interest_income += interest

            borrower.profit -= interest

            return True

        self.default_loan(borrower)
        return False

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

        if borrower.loan <= 0:
            borrower.loan_interest_rate = 0.0
            self.number_of_loans = max(
                0,
                self.number_of_loans - 1
            )

        return True

    def credit_score(self, borrower):
        score = 100

        if borrower.money <= 100:
            score -= 30

        if borrower.profit < 0:
            score -= 30

        if borrower.loan > borrower.maximum_debt * 0.75:
            score -= 20

        return max(0, score)

    def get_loan_interest_rate(self, borrower):
        score = self.credit_score(borrower)

        if score >= 80:
            return 0.05

        if score >= 60:
            return 0.07

        if score >= 50:
            return 0.10

        return None

    def assess_credit(self, borrower, amount):
        if amount <= 0:
            return False

        if amount > self.maximum_loan:
            return False

        if borrower.loan + amount > borrower.maximum_debt:
            return False

        interest_rate = self.get_loan_interest_rate(borrower)

        if interest_rate is None:
            return False

        projected_capital_ratio = (
            self.projected_capital_ratio(amount)
        )

        if projected_capital_ratio < self.minimum_capital_ratio:
            return False

        projected_liquidity_ratio = (
            self.projected_liquidity_ratio(amount)
        )

        if projected_liquidity_ratio < self.minimum_liquidity_ratio:
            return False

        return True

    def default_loan(self, borrower):
        loan_amount = borrower.loan

        if loan_amount <= 0:
            return 0.0

        self.defaulted_loans += 1
        self.loan_losses += loan_amount

        self.loans -= loan_amount

        # Remove the corresponding deposit created by the loan.
        self.deposits = max(
            0.0,
            self.deposits - loan_amount
        )

        borrower.loan = 0.0
        borrower.loan_interest_rate = 0.0

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
            return 0.0

        return self.calculate_capital() / assets

    def liquidity_ratio(self):
        if self.deposits <= 0:
            return float("inf")

        return self.reserves / self.deposits

    def projected_capital_ratio(self, amount):
        projected_assets = self.total_assets() + amount

        if projected_assets <= 0:
            return 0.0

        capital = self.calculate_capital()

        return capital / projected_assets

    def projected_liquidity_ratio(self, amount):
        projected_deposits = self.deposits + amount

        if projected_deposits <= 0:
            return float("inf")

        return self.reserves / projected_deposits
