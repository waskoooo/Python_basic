lenght = int(input())
wide = int(input())
height = int(input())
percent = float(input())

volume = lenght * wide * height
volume_in_liters = volume * 0.001
space_taken = 0.17

liters_needed = volume_in_liters * (1-space_taken)

print(liters_needed)