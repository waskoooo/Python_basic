hall_rent = int(input())

statues = hall_rent * 0.70
catering = statues * 0.85
sounding = catering / 2

all_cost = hall_rent + statues + catering + sounding

print(f"{all_cost:.2f}")