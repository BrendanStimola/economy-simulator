from World import World


economy = World()

days = input("How many days?")

days = int(days)

for firm in economy.firms:
    rating = economy.bank.credit_score(firm)

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
            f"Rating: {rating:.2f}"
        )

    print("\nHouseholds:")

    for i, household in enumerate(economy.households):

        print(
            f"Household {i + 1} | "
            f"Money: ${household.money:.2f} | "
            f"Goods: {household.goods}"
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
        f"Deposit Interest: "
        f"${economy.bank.deposit_interest:.2f}"
    )

    print(
        f"Interest Income: "
        f"${economy.bank.interest_income:.2f}"
    )

    print(
        f"Defaulted Loans: "
        f"{economy.bank.defaulted_loans}"
    )

    print(
        f"Loan Losses: "
        f"${economy.bank.loan_losses:.2f}"
    )

    print(
        f"Bank Assets: "
        f"${economy.bank.total_assets():.2f}"
    )

    print(
        f"Bank Liabilities: "
        f"${economy.bank.total_liabilities():.2f}"
        )

    print(
        f"Bank Capital: "
        f"${economy.bank.calculate_capital():.2f}"
    )

    print(
        f"Capital Ratio: "
        f"{economy.bank.capital_ratio() * 100:.2f}%"
    )

    print(
        f"Minimum Capital Ratio: "
        f"{economy.bank.minimum_capital_ratio * 100:.2f}%"
    )

    print(
        f"Liquidity Ratio: "
        f"{economy.bank.liquidity_ratio() * 100:.2f}%"
    )