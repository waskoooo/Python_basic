import math

SUGAR = 950
FLOUR = 750

easter_breads_number = int(input())
all_sugar = 0
all_flour = 0
max_sugar = 0
max_flour = 0
"""
1
"""
# for _ in range(easter_breads_number):
#     sugar = int(input())
#     all_sugar += sugar
#     flour = int(input())
#     all_flour += flour
#
#     if sugar > max_sugar:
#         max_sugar = sugar
#
#     if flour > max_flour:
#     max_flour = flour
"""
2
"""
# current_easter_bread = 1
# while current_easter_bread <= easter_breads_number:
#     sugar = int(input())
#     all_sugar += sugar
#     flour = int(input())
#     all_flour += flour
#
#     if sugar > max_sugar:
#         max_sugar = sugar
#
#     if flour > max_flour:
#         max_flour = flour
#
#     current_easter_bread += 1
"""
3
"""
current_easter_bread = 1
while True:
    if current_easter_bread > easter_breads_number:
        break
    sugar = int(input())
    all_sugar += sugar
    flour = int(input())
    all_flour += flour

    if sugar > max_sugar:
        max_sugar = sugar

    if flour > max_flour:
        max_flour = flour

    current_easter_bread += 1

print(f'Sugar: {math.ceil(all_sugar / SUGAR)}')
print(f'Flour: {math.ceil(all_flour / FLOUR)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
