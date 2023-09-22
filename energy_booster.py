gel_type_fruit = input()   # watermelon , mango , pineapple , raspberry
packet_type = input()       # big or small
count_pack = float(input())

packet_type_cost = 0

if gel_type_fruit == "Watermelon":
    if packet_type == "small":
        packet_type_cost = 56 * 2
    elif packet_type == "big":
        packet_type_cost = 28.70 * 5

elif gel_type_fruit == "Mango":
    if packet_type == "small":
        packet_type_cost = 36.66 * 2
    elif packet_type == "big":
        packet_type_cost = 19.60 * 5

elif gel_type_fruit == "Pineapple":
    if packet_type == "small":
        packet_type_cost = 42.10 * 2
    elif packet_type == "big":
        packet_type_cost = 24.80 * 5

elif gel_type_fruit == "Raspberry":
    if packet_type == "small":
        packet_type_cost = 20 * 2
    elif packet_type == "big":
        packet_type_cost = 15.20 * 5

set_price = count_pack * packet_type_cost

if 400 <= set_price <= 1000:
    set_price = set_price * 0.85

elif set_price > 1000:
    set_price = set_price * 0.50

print(f"{set_price:.2f} lv.")
