luggage_over_20 = float(input())
luggage_in_kg = float(input())
days_to_strip = int(input())
number_of_bags = int(input())

price = 0


if luggage_in_kg < 10 :
    price = luggage_over_20 * 0.20
elif 10 <= luggage_in_kg <= 20:
    price = luggage_over_20 * 0.50
elif 20 < luggage_in_kg:
    price = luggage_over_20

if days_to_strip < 7:
    price = price * 1.40
elif 7 <= days_to_strip <= 30:
    price = price * 1.15
elif 30 < days_to_strip :
    price = price * 1.10

final_cost = number_of_bags * price

print(f"The total price of bags is: {final_cost:.2f} lv.")
