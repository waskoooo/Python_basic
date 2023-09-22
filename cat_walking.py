minutes_walk = int(input())
walks_per_day = int(input())
calories_taken = int(input())

all_minutes_walk = walks_per_day * minutes_walk
calories_burnt = all_minutes_walk * 5

calories_take_vs_burnt = (calories_burnt/calories_taken) * 100

if calories_take_vs_burnt >= 50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
elif calories_take_vs_burnt < 50:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")
