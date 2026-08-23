class Firm:
    def __init__(self, name):
        self.name = name

        # Financial position
        self.money = 500.0
        self.deposit = 0.0
        self.loan = 0.0

        # Production
        self.inventory = 12
        self.price = 20.0
        self.production = 10.0

        # Sales and income
        self.sales = 0
        self.revenue = 0.0
        self.profit = 0.0

        # Debt
        self.maximum_debt = 100.0
        self.loan_interest_rate = 0.0

        # Production/investment
        self.minimum_price = 1.0
        self.investment_need = 50.0

        # Labor
        self.workers = []
        self.wages = 20.0
        self.wage_bill = 0.0

    def produce(self):
        self.inventory += self.production

    def adjust_price(self, competitors):
        if self.inventory < 5:
            self.price += 0.50

        elif self.inventory > 20:
            self.price = max(
                self.minimum_price,
                self.price - 0.50
            )

        if competitors:
            average_price = (
                sum(firm.price for firm in competitors)
                / len(competitors)
            )

            if self.inventory > 20 and average_price < self.price:
                self.price -= 0.25

            elif self.inventory < 5 and average_price > self.price:
                self.price += 0.25

        self.price = max(
            self.price,
            self.minimum_price
        )

    def invest(self, amount):
        if amount <= 0:
            return False

        if self.money < amount:
            return False

        self.money -= amount
        self.production += amount / 10

        return True

    def wants_loan(self):
        if self.money < 600:
            return True

        if self.inventory <= 20:
            return True

        return False

    def pay_wages(self):
        self.wage_bill = 0.0

        for worker in self.workers:
            if self.money < self.wages:
                break

            self.money -= self.wages

            worker.money += self.wages
            worker.wage_income += self.wages
            worker.total_income += self.wages

            self.wage_bill += self.wages

    def calculate_profit(self):
        interest_expense = (
            self.loan * self.loan_interest_rate / 365
        )

        self.profit = (
            self.revenue
            - self.wage_bill
            - interest_expense
        )

        return self.profit

    def reset_daily_financials(self):
        self.sales = 0
        self.revenue = 0.0
        self.wage_bill = 0.0
        self.profit = 0.0
