month = input()
stay = int(input())

studio = 0
apartment = 0


if month == 'May' or month == 'October':
    studio = 50
    if stay > 14:
        studio = 50 * 0.70
    elif stay > 7:
        studio = 50 * 0.95

    apartment = 65
    if stay > 14:
        apartment = 65 * 0.90

elif month == 'June' or month == 'September':
    studio = 75.20
    if stay > 14:
        studio = 75.20 * 0.80
    apartment = 68.70
    if stay > 14:
        apartment = 68.70 * 0.90


elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if stay > 14:
        apartment = 77 * 0.9

print(f'Apartment: {stay * apartment:.2f} lv.')
print(f'Studio: {stay * studio:.2f} lv.')
