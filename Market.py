class Market: 
    def __init__(self):

        self.transactions = 0

    def run(self, households, firms):

        for household in households:

            firm = firms[0]

            household.buy(firm)

            self.transactions += 1