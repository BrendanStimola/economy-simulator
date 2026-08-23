from World import World


economy = World()

days = int(input("How many days? "))

for _ in range(days):
    economy.update()

    print(f"\n--- Day {economy.day} ---")

    print("\nFirms:")

    for firm in economy.firms:
        print(
            f"{firm.name} | "
            f"Money: ${firm.money:.2f} | "
            f"Inventory: {firm.inventory:.2f} | "
            f"Price: ${firm.price:.2f} | "
            f"Sales: {firm.sales} | "
            f"Revenue: ${firm.revenue:.2f} | "
            f"Profit: ${firm.profit:.2f} | "
            f"Rating: {economy.bank.credit_score(firm)} | "
            f"Loan: ${firm.loan:.2f}"
        )

    print("\nHouseholds:")

    for i, household in enumerate(economy.households):
        print(
            f"Household {i + 1} | "
            f"Money: ${household.money:.2f} | "
            f"Deposit: ${household.deposit:.2f} | "
            f"Wealth: ${household.financial_wealth():.2f} | "
            f"Income: ${household.total_income:.2f} | "
            f"Consumption: ${household.consumption:.2f} | "
            f"Goods: {household.goods}"
        )

    print("\nGovernment:")

    print(
        f"Revenue: "
        f"${economy.government.revenue:.2f}"
    )

    print(
        f"Spending: "
        f"${economy.government.spending:.2f}"
    )

    print(
        f"Budget Balance: "
        f"${economy.government.budget_balance:.2f}"
    )

    print(
        f"Debt: "
        f"${economy.government.debt:.2f}"
    )

    print("\n--- Bank ---")

    print(
        f"Deposits: "
        f"${economy.bank.deposits:.2f}"
    )

    print(
        f"Loans: "
        f"${economy.bank.loans:.2f}"
    )

    print(
        f"Reserves: "
        f"${economy.bank.reserves:.2f}"
    )

    print(
        f"Assets: "
        f"${economy.bank.total_assets():.2f}"
    )

    print(
        f"Liabilities: "
        f"${economy.bank.total_liabilities():.2f}"
    )

    print(
        f"Capital: "
        f"${economy.bank.calculate_capital():.2f}"
    )

    print(
        f"Capital Ratio: "
        f"{economy.bank.capital_ratio():.2%}"
    )

    print(
        f"Liquidity Ratio: "
        f"{economy.bank.liquidity_ratio():.2%}"
    )

    print(
        f"Defaulted Loans: "
        f"{economy.bank.defaulted_loans}"
    )
