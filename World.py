from Household import Household
from Firm import Firm
from Market import Market
from Government import Government

class World:
    def __init__(self):

        self.day = 0

        self.households = []

        self.firms = []

        self.market = Market()

        self.government = Government()

        self.create_world()

    def create_world(self):

        for i in range(10):

            self.households.append(
                Household()
            )

        for i in range(3):

            self.firms.append(
                Firm(f"Firm {i + 1}")
            )
    def update(self):

        self.day += 1

        for firm in self.firms:
            
            firm.produce()

        self.market.run(

            self.households, 

            self.firms
        )

        self.government.collect_taxes(self.households)

        self.government.spend(self.households)

        self.government.update_budget()