import sys

player_name = input()
name = ""

max_goals = -sys.maxsize

while player_name != "END":
    goal = int(input())
    if goal > max_goals:
        max_goals = goal
        name = player_name
    if goal >= 10:
        break
    player_name = input()

print(f"{name} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
elif max_goals < 3:
    print(f"He has scored {max_goals} goals.")




