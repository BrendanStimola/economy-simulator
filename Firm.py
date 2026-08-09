class Firm:
    def __init__(self, name):

        self.name = name

        self.money = 500

        self.inventory = 12

        self.price = 20

        self.production = 10

        self.sales = 0

        self.deposit = 0

        self.loan = 0

        self.revenue = 0

        self.profit = 0

        self.maximum_debt = 100

        self.minimum_price = 1

        self.investment_need = 50

        self.workers = []

        self.wages = 20

        self.wage_bill = 0

    def produce(self):

        self.inventory += self.production

    def adjust_price(self, competitors):

        if self.inventory < 5:

            self.price += 0.5

        if self.inventory > 20:

            self.price = max(self.minimum_price, self.price - 0.50)

        if competitors:

            average_price = sum(firm.price for firm in competitors)/len(competitors)

            if self.inventory > 20 and average_price < self.price:
                self.price -= 0.25
            elif self.inventory < 5 and average_price > self.price:
                self.price += 0.25
        self.price = max(self.price, self.minimum_price)

    def invest(self, amount):

        if self.money >= amount:

            self.money -= amount

            self.production += amount/10

            return True
        
        return False

    def wants_loan(self):
        if self.money < 600:
            return True
        elif self.inventory <= 20:
            return True
        else:
            return False

    def pay_wages(self):
        self.wage_bill = 0
        for worker in self.workers:
            if self.money < self.wages:
                break
            self.money -= self.wages
            worker.money += self.wages
            worker.wage_income += self.wages
            worker.total_income += self.wages
            self.wage_bill += self.wages
