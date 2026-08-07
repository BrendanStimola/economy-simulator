from Household import Household
from Firm import Firm
from Market import Market

class World:
    def __init__(self):

        self.day = 0

        self.households = []

        self.firms = []

        self.market = Market()

        self.create_world()

    def create_world(self):

        for i in range(10):

            self.households.append(Household())

        for i in range(3):

            self.firms.append(Firm())

    def update(self):

        self.day += 1

        for firm in self.firms:
            
            firm.produce()

        self.market.run(

            self.households, 

            self.firms
        )