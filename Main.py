from World import World

economy = World()

print("Households:", len(economy.households))
print()
print("Firms:", len(economy.firms))
print()

for day in range(10):

    economy.update()

    print("Current day:", economy.day)
    print()
    print("Firm Money:", economy.firms[0].money)
    print()
    print("Firm Inventory:", economy.firms[0].invetory)
    print()
    print("Household Money:", economy.households[0].money)
    print()
    print("Household Goods:", economy.households[0].goods)
    print()