CHICKEN = 10.35
FISH = 12.40
VEGAN = 8.15
DELIVERY = 2.50

chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

order_price = chicken_menu * CHICKEN + fish_menu * FISH + vegan_menu * VEGAN

desert = order_price * 0.20

end_sum = order_price + desert + DELIVERY

print(end_sum)