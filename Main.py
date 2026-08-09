from World import World


economy = World()

days = input("How many days?")

days = int(days)

for i in range(days):

    economy.update()

    print(f"\n--- Day {economy.day} ---")

    print("\nFirms:")

    for firm in economy.firms:

        print(
            f"{firm.name} | "
            f"Money: ${firm.money:.2f} | "
            f"Inventory: {firm.inventory} | "
            f"Price: ${firm.price:.2f} | "
            f"Sales: {firm.sales} | "
            f"Rating: {economy.bank.credit_score(firm):.2f} | "
            f"Loan: ${firm.loan:.2f} | "
        )

    print("\nHouseholds:")

    for i, household in enumerate(economy.households):

        print(
            f"Household {i + 1} | "
            f"Money: ${household.money:.2f} | "
            f"Savings: ${household.savings:.2f} | "
            f"Goods: {household.goods} | "
        )
        
    print("\nGovernment:")

    print(
        f"Revenue: ${economy.government.revenue:.2f}"
    )

    print(
        f"Spending: ${economy.government.spending:.2f}"
    )

    print(
        f"Budget Balance: "
        f"${economy.government.budget_balance:.2f}"
    )

    print(
        f"Debt: ${economy.government.debt:.2f}"
    )

    print("\n--- Bank ---")

    print(f"Deposits: ${economy.bank.deposits:.2f}")
    print(f"Loans: ${economy.bank.loans:.2f}")
    print(f"Reserves: ${economy.bank.reserves:.2f}")   
    print(f"Assets: ${economy.bank.total_assets():.2f}")
    print(f"Liabilities: ${economy.bank.total_liabilities():.2f}")
    print(f"Capital: ${economy.bank.calculate_capital():.2f}")
    print(f"Capital Ratio: {economy.bank.capital_ratio():.2%}")
    print(f"Liquidity Ratio: {economy.bank.liquidity_ratio():.2%}")
    print(f"Defaulted Loans: {economy.bank.defaulted_loans}")