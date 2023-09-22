import math

money_client_have = float(input())
gender = input()
age = int(input())
type_of_sport = input()

sport_price = 0


if gender == "m":
    if type_of_sport == "Gym":
        sport_price = 42
    elif type_of_sport == "Boxing":
        sport_price = 41
    elif type_of_sport == "Yoga":
        sport_price = 45
    elif type_of_sport == "Zumba":
        sport_price = 34
    elif type_of_sport == "Dances":
        sport_price = 51
    elif type_of_sport == "Pilates":
        sport_price = 39

if gender == "f":
    if type_of_sport == "Gym":
        sport_price = 35
    elif type_of_sport == "Boxing":
        sport_price = 37
    elif type_of_sport == "Yoga":
        sport_price = 42
    elif type_of_sport == "Zumba":
        sport_price = 31
    elif type_of_sport == "Dances":
        sport_price = 53
    elif type_of_sport == "Pilates":
        sport_price = 37

if age <= 19:
    sport_price = sport_price * 0.80

if sport_price <= money_client_have:
    print(f"You purchased a {math.floor(money_client_have / sport_price)} month pass for {type_of_sport}.")

elif sport_price > money_client_have:
    print(f"You don't have enough money! You need ${sport_price - money_client_have:.2f} more.")