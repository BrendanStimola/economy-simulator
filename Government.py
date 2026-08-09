class Government:

    def __init__(self):

        self.tax_rate = 0.2

        self.spending = 100

        self.revenue = 0

        self.debt = 1000

        self.budget_balance = 0

    def collect_household_taxes(self, households):

        self.revenue = 0

        for household in households:

            tax = household.wage_income * self.tax_rate

            household.wage_income -= tax

            self.revenue += tax

    def spend(self, households):

        payment = self.spending / len(households)

        for household in households:
            
            household.transfer_income += payment

    def update_budget(self):

        self.budget_balance = self.revenue - self.spending

        if self.budget_balance < 0:

            self.debt += abs(self.budget_balance)

        else:

            self.debt -= self.budget_balance