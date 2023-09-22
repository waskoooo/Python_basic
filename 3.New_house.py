type_flower = input()
number_flowers = int(input())
budget = int(input())

final_price = 0

if type_flower == 'Roses':
    final_price = number_flowers * 5
    if number_flowers > 80:
        final_price = final_price * 0.90

elif type_flower == 'Dahlias':
    final_price = number_flowers * 3.80
    if number_flowers > 90:
        final_price = final_price * 0.85

elif type_flower == 'Tulips':
    final_price = number_flowers * 2.80
    if number_flowers > 80:
        final_price = final_price * 0.85

elif type_flower == 'Narcissus':
    final_price = number_flowers * 3
    if number_flowers < 120:
        final_price = final_price * 1.15

elif type_flower == 'Gladiolus':
    final_price = number_flowers *2.50
    if number_flowers < 80:
        final_price = final_price * 1.20

if budget >= final_price:
    print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {budget - final_price:.2f} leva left. ")

elif budget < final_price:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")