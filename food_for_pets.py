import math

days = int(input())
food = float(input())

total = 0
dog = 0
cat = 0
biscuits = 0
biscuits_total = 0

for i in range(1, days + 1):
    food_eaten_by_dog = int(input())
    dog += food_eaten_by_dog
    food_eaten_by_cat = int(input())
    cat += food_eaten_by_cat
    total += food_eaten_by_cat + food_eaten_by_dog
    if i % 3 == 0:
        biscuits += (food_eaten_by_cat + food_eaten_by_dog) * 0.10

biscuits_total = round(biscuits)

print(f'Total eaten biscuits: {biscuits_total}gr.')
print(f'{total / food * 100:.2f}% of the food has been eaten.')
print(f'{dog / total * 100:.2f}% eaten from the dog.')
print(f'{cat / total * 100:.2f}% eaten from the cat.')