target = int(input())  # Цел за деня
total_money = 0

while True:
    command = input()  # Вид услуга - "haircut" или "color"

    if command == "closed":
        break

    service = input()  # Вид на подстригване или боядисване

    if command == "haircut":
        if service == "mens":
            total_money += 15
        elif service == "ladies":
            total_money += 20
        elif service == "kids":
            total_money += 10
    elif command == "color":
        if service == "touch up":
            total_money += 20
        elif service == "full color":
            total_money += 30

    if total_money >= target:
        print("You have reached your target for the day!")
        break

if total_money < target:
    needed_money = target - total_money
    print(f"Target not reached! You need {needed_money}lv. more.")

print(f"Earned money: {total_money}lv.")
