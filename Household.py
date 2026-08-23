import random


class Household:
    def __init__(self, name):
        self.name = name

        # Financial assets
        self.money = 100.0
        self.deposit = 0.0

        # Debt
        self.loan = 0.0

        # Physical goods
        self.goods = 0

        # Income
        self.wage_income = 0.0
        self.transfer_income = 0.0
        self.interest_income = 0.0
        self.total_income = 0.0

        # Spending
        self.consumption = 0.0

    def reset_daily_income(self):
        self.wage_income = 0.0
        self.transfer_income = 0.0
        self.interest_income = 0.0
        self.total_income = 0.0
        self.consumption = 0.0
        self.goods = 0

    def calculate_total_income(self):
        self.total_income = (
            self.wage_income
            + self.transfer_income
            + self.interest_income
        )
        return self.total_income

    def financial_wealth(self):
        return self.money + self.deposit

    def buy(self, firms):
        spending_limit = self.total_income * 0.80

        while (
            self.consumption < spending_limit
            and self.money > 0
        ):
            affordable = [
                firm
                for firm in firms
                if self.money >= firm.price and firm.inventory > 0
            ]

            if not affordable:
                break

            cheapest = min(
                affordable,
                key=lambda firm: firm.price
            )

            self.money -= cheapest.price
            cheapest.money += cheapest.price

            cheapest.inventory -= 1
            cheapest.sales += 1
            cheapest.revenue += cheapest.price

            self.consumption += cheapest.price
            self.goods += 1

    def wants_to_withdraw(self):
        if self.deposit > 20:
            return random.random() < 0.5

        return False
