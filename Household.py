class Household:
    def __init__(self):

        self.money = 100

        self.goods = 0

        self.job = False

    def buy(self, firm):

        if self.money >= firm.price and firm.invetory > 0:

            self.money -= firm.price

            self.goods += 1

            firm.invetory -= 1

            firm.money += firm.price