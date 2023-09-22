house_height = float(input())
wall_width = float(input())
roof_wall = float(input())

#house walls

side_wall = house_height * wall_width
window = 1.5 * 1.5

both_side_walls = (side_wall * 2) - (2*window)

back_wall = house_height * house_height
door = 1.2*2

back_fron_wall = (back_wall *2) - door

green_side = both_side_walls + back_fron_wall
green_paint = green_side / 3.4
#roof

both_sides_roof = 2 * (house_height * wall_width)
front_back_roof = (house_height * roof_wall)
all_roof = both_sides_roof + front_back_roof
red_paint = all_roof / 4.3


print(f'{green_paint:.2f} ')
print(f"{red_paint:.2f}")