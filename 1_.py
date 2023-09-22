rolls_count = int(input())
rolls_fabric = int(input())
glue_liters = float(input())
discount = int(input())

rolls_price = 5.80
fabric_price = 7.20
glue_price = 1.20


all_cost = rolls_count * rolls_price + rolls_fabric * fabric_price + glue_liters * glue_price

discount_amount = all_cost * (discount / 100)

print(f"{all_cost - discount_amount:.3f}")

