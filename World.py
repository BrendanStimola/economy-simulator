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

        self.firms[0].workers = self.households[0:4]

        self.firms[1].workers = self.households[4:7]

        self.firms[2].workers = self.households[7:10]

    def create_world(self):

        for i in range(10):

            self.households.append(
                Household(f"Household {i + 1}")
            )

        for i in range(3):

            self.firms.append(
                Firm(f"Firm {i + 1}")
            )

    def banking_activity(self):

        for household in self.households:

            if household.money > 80:

                self.bank.deposit(household, 20)

                household.savings += 20

        for household in self.households:

            self.bank.pay_deposit_interest(household)

        for household in self.households:

            if household.wants_to_withdraw():

                amount = min(household.deposit, 20)

                if amount > 0:
                    withdrawn = self.bank.withdraw(household, 20)

                    if withdrawn:

                        household.savings -= amount
                        
                        print(

                            f"{household.name} "

                            f"withdrew ${amount:.2f} and has ${household.savings:.2f} savings left"

                        )

                    else:

                        print(

                            f"{household.name} "

                            f"could not withdraw"

                        )


        for firm in self.firms:

            if firm.loan > 0:

                paid = self.bank.process_loan_payments(firm)


                if paid:

                    print(

                        f"{firm.name} paid loan interest"

                    )

                else:

                    print(

                        f"{firm.name} DEFAULTED"
                    )

        for firm in self.firms:

            if firm.wants_loan():

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

    def pricing_activity(self):
        for firm in self.firms:
            competitors = [other for other in self.firms if other != firm]
            firm.adjust_price(competitors)
    
    def update(self):

        self.day += 1

        for household in self.households:
            household.reset_daily_income()

        for firm in self.firms:
            firm.pay_wages()

        self.banking_activity()

        for firm in self.firms:
            firm.produce()

        self.market.run(
            self.households,
            self.firms
        )

        self.pricing_activity()

        self.government.collect_household_taxes(
            self.households
        )

        self.government.spend(
            self.households
        )

        self.government.update_budget()