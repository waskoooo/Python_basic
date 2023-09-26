import math

MAGNOLIA = 3.25
ZUMBULS = 4
ROSES = 3.5
CACTUS = 8

dds = 0.05

magnolia_count = int(input())
zumbuls_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

all_cost = MAGNOLIA * magnolia_count + ZUMBULS *zumbuls_count + ROSES * roses_count + CACTUS * cactus_count
all_cost_with_dds = all_cost * dds

end_sum = all_cost_with_dds + all_cost

if end_sum < gift_price:
    print(f"She is left with {math.floor(gift_price - end_sum)} leva.")

elif end_sum > gift_price:
    print(f"She will have to borrow {math.ceil(end_sum - gift_price)} leva.")

#fix
