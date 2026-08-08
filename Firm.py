class Firm:
    def __init__(self, name):

        self.name = name

        self.money = 500

        self.inventory = 12

        self.price = 10

        self.production = 3

        self.sales = 0

        self.deposit = 0

        self.loan = 0

    def produce(self):

        self.inventory += self.production

    def adjust_price(self):

        if self.inventory < 4:

            self.price *= 1.05

        if self.inventory > 10:

            self.price *= 0.95

    def invest(self, amount):

        if self.money >= amount:

            self.money -= amount

            self.production += 1

            return True
        
        return False