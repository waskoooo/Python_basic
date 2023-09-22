while True:
    destination = input()

    if destination == "End":
        break

    budget = float(input())
    total_saved = 0

    while total_saved < budget:
        saved_money = float(input())
        total_saved += saved_money

    print(f"Going to {destination}!")