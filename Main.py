from World import World


economy = World()


for i in range(10):

    economy.update()

    print(f"\n--- Day {economy.day} ---")

    print("\nFirms:")

    for firm in economy.firms:

        print(
            f"{firm.name} | "
            f"Money: ${firm.money:.2f} | "
            f"Inventory: {firm.inventory} | "
            f"Price: ${firm.price:.2f} | "
            f"Sales: {firm.sales}"
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