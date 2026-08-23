class Market:
    def __init__(self):
        self.transactions = 0
        self.total_sales = 0.0

    def run(self, households, firms):
        self.transactions = 0
        self.total_sales = 0.0

        for firm in firms:
            firm.reset_daily_financials()

        for household in households:
            before_consumption = household.consumption

            household.calculate_total_income()
            household.buy(firms)

            if household.consumption > before_consumption:
                self.transactions += 1
                self.total_sales += (
                    household.consumption
                    - before_consumption
                )
