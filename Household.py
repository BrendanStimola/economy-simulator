import random

class Household:
    def __init__(self, name):

        self.money = 100

        self.goods = 0

        self.deposit = 0

        self.loan = 0

        self.wage_income = 0

        self.transfer_income = 0

        self.interest_income = 0

        self.total_income = 0

        self.consumption = 0

        self.savings = 0

        self.name = name

    def reset_daily_income(self):
        self.wage_income = 0
        self.transfer_income = 0
        self.interest_income = 0
        self.total_income = 0
        self.consumption = 0
        self.goods = 0

    def buy(self, firms):

        while self.consumption < self.total_income * 0.8 and self.money > 0:

            affordable = []

            for firm in firms:

                if self.money >= firm.price and firm.inventory > 0:

                    affordable.append(firm)


            if len(affordable) > 0:

                cheapest = min(affordable, key=lambda firm: firm.price)

                self.money -= cheapest.price

                self.consumption += cheapest.price

                self.goods += 1

                cheapest.money += cheapest.price

                cheapest.inventory -= 1

                cheapest.sales += 1

            else:
                
                break

    def wants_to_withdraw(self):
        if self.deposit > 20:
            if random.random() < 0.5:
                return True
        return False