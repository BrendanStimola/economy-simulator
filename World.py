from Household import Household
from Firm import Firm
from Market import Market
from Government import Government
from Bank import Bank

class World:
    def __init__(self):

        self.day = 0

        self.households = []

        self.firms = []

        self.market = Market()

        self.government = Government()

        self.bank = Bank()

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

    def banking_activity(self):

        for household in self.households:

            if household.money > 80:

                self.bank.deposit(household, 20)

        for household in self.households:

            self.bank.pay_deposit_interest(household)

        for firm in self.firms:

            if firm.inventory <= 10:

                score = self.bank.credit_score(firm)

                rate = self.bank.get_loan_interest_rate(firm)

                print(
                f"{firm.name}: "
                f"Credit Score = {score}, "
                f"Loan Rate = {rate}"
                )

            loan_given = self.bank.lend(

                firm,
                50
            )

            if loan_given:

                print(

                    f"{firm.name} borrowed $50"
                )

                firm.invest(50)

            else:

                print(

                    f"{firm.name} loan rejected"
                )
    
    def update(self):

        self.day += 1

        self.bank.deposit_interest = 0

        for firm in self.firms:
            
            firm.produce()

        self.market.run(

            self.households, 

            self.firms
        )

        self.banking_activity()

        self.government.collect_household_taxes(self.households)

        self.government.spend(self.households)

        self.government.update_budget()