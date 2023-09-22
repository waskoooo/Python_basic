import math

width = float(input()) * 100
height = float(input()) * 100

space_height_left = math.floor((height - 100) / 70)
space_width_left = math.floor(width / 120)

spaces = (space_width_left * space_height_left) - 3

print(f"{spaces:.0f}")
