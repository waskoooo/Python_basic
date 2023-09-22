budget = float(input())
season = input()

destination = ''
type_stay = ''
price_stay = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        type_stay = 'Camp'
        price_stay = budget * 0.30
    elif season == 'winter':
        type_stay = 'Hotel'
        price_stay = budget * 0.70

elif 101 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        type_stay = 'Camp'
        price_stay = budget * 0.40
    elif season == 'winter':
        type_stay = 'Hotel'
        price_stay = budget * 0.80

elif budget > 1000:
    destination = 'Europe'
    type_stay = 'Hotel'
    price_stay = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type_stay} - {price_stay:.2f} ")


