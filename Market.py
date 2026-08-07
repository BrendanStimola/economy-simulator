class Market: 
    def __init__(self):

        self.transactions = 0

    def run(self, households, firms):

        for firm in firms:

            firm.sales = 0

        for household in households:

            household.buy(firms)

            self.transactions += 1

            for firm in firms:
                firm.adjust_price()