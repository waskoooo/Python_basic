import math

show_name = input()
duration_episode = int(input())
duration_break = int(input())

time_for_lunch = duration_break / 8
time_for_break = duration_break / 4

time_left = duration_break - time_for_lunch - time_for_break
time_for_episode = math.ceil(time_left - duration_episode)

if time_left >= duration_episode:
    print(f'You have enough time to watch {show_name} and left with {time_for_episode} minutes free time. ')
elif time_left <= duration_episode:
    time_episode = math.ceil(duration_episode - time_left) #duration_episode - time_left
    print(f"You don't have enough time to watch {show_name}, you need {time_episode} more minutes.")

    #f"You don't have enough time to watch {tvseries}, you need {needed} more minutes."