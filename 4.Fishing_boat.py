budget = int(input())
season = input()
fishermen = int(input())

ship_cost = 0
ship_discount = 0

if season == 'Spring':
    ship_cost = 3000
elif season == 'Summer':
    ship_cost = 4200
elif season == 'Autumn':
    ship_cost = 4200
elif season == 'Winter':
    ship_cost = 2600

if fishermen <= 6:
    ship_discount = ship_cost * 0.90
elif fishermen <= 11:
    ship_discount = ship_cost * 0.85
elif fishermen > 12:
    ship_discount = ship_cost * 0.75

if fishermen % 2 == 0 and season != 'Autumn':
    ship_discount = ship_discount * 0.95

if budget >= ship_discount:
    print(f'Yes! You have {budget - ship_discount :.2f} leva left.')
elif ship_discount >= budget:
    print(f'Not enough money! You need {ship_discount - budget:.2f} leva.')
