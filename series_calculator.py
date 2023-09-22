def calculate_total_time(seasons, episodes_per_season, episode_duration):
    total_time = 0

    for season in range(1, seasons + 1):
        for episode in range(1, episodes_per_season + 1):
            episode_time = episode_duration + 0.2 * episode_duration  # Време на епизод + 20% реклами
            total_time += episode_time

        if season != seasons:
            total_time += 10  # 10 минути на края на сезона

    return total_time


# Въвеждане на данните от потребителя
serial_name = input()
seasons = int(input())
episodes_per_season = int(input())
episode_duration = float(input())

total_time_minutes = calculate_total_time(seasons, episodes_per_season, episode_duration)
print(f"Total time needed to watch the {serial_name} series is {10 + total_time_minutes:.0f} minutes.")
