actor = input()
starting_points = float(input())
judges_count = int(input())

total_points = starting_points

for _ in range(1, judges_count + 1):
    judge_name = input()
    judge_points = float(input())
    total_points += len(judge_name) * judge_points / 2
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {1250.5 - total_points:.1f} more!")