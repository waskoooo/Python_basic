name = input()
adult_ticket_count = int(input())
kid_ticket_count = int(input())
price_adult = float(input())
service_price = float(input())

kid_price = price_adult * 0.30

price_adult_service = price_adult + service_price
kid_price_service = kid_price + service_price

all_cost = adult_ticket_count * price_adult_service + kid_ticket_count * kid_price_service

profit_money = all_cost * 0.20

print(f"The profit of your agency from {name} tickets is {profit_money:.2f} lv.")