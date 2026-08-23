class Government:
    def __init__(self):
        self.tax_rate = 0.20

        self.spending = 100.0
        self.revenue = 0.0

        self.debt = 1000.0
        self.budget_balance = 0.0

    def collect_household_taxes(self, households):
        self.revenue = 0.0

        for household in households:
            tax = household.wage_income * self.tax_rate

            if tax <= 0:
                continue

            tax = min(tax, household.money)

            household.money -= tax
            self.revenue += tax

    def spend(self, households):
        if not households:
            return

        payment = self.spending / len(households)

        for household in households:
            household.money += payment
            household.transfer_income += payment

    def update_budget(self):
        self.budget_balance = (
            self.revenue - self.spending
        )

        if self.budget_balance < 0:
            self.debt += abs(self.budget_balance)

        else:
            self.debt = max(
                0.0,
                self.debt - self.budget_balance
            )
