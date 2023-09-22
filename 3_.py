dancers_count = int(input())
points_count = float(input())
season = input()
destination = input()

money_price = dancers_count * points_count
money_abroad = 0

if destination == "Bulgaria":
    if season == "summer":
        money_price = money_price * 0.95
    elif season == "winter":
        money_price = money_price * 0.92

elif destination == "Abroad":
    money_price = money_price / 2 + money_price
    if season == "summer":
        money_price = money_price * 0.90
    elif season == "winter":
        money_price = money_price * 0.85


charity = money_price * 0.75
money_left = money_price - charity
dancers_money = money_left / dancers_count

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {dancers_money:.2f}")