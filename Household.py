from World import World

class Household:
    def __init__(self):

        self.money = 100

        self.goods = 0

        self.job = False

    def buy(self, firms):

        affordable = []

        for firm in firms:

            if self.money >= firm.price and firm.inventory > 0:

                affordable.append(firm)


        if len(affordable) > 0:

            cheapest = min(affordable, key=lambda firm: firm.price)

            self.money -= cheapest.price

            self.goods += 1

            cheapest.money += cheapest.price

            cheapest.inventory -= 1

            cheapest.sales += 1