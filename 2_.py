t_shirt_price = float(input())
price_must_reach = float(input())       # cena za topkata koqto trqbwa da napravi

shorts_price = t_shirt_price * 0.75
socs_price = shorts_price * 0.20
shoes_price = (t_shirt_price + shorts_price) * 2

all_cost = t_shirt_price + shorts_price + socs_price +shoes_price
all_cost_discount = all_cost * 0.85

if all_cost_discount > price_must_reach:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {all_cost_discount:.2f} lv.")

elif all_cost_discount < price_must_reach:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {price_must_reach - all_cost_discount:.2f} lv. more.")