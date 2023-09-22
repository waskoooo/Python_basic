import math

record_in_seconds = float(input())
distance_in_meters = float(input())
one_meter_in_seconds = float(input())

distance_to_clim = distance_in_meters * one_meter_in_seconds
slow_down = math.floor(distance_in_meters / 50)
slow_down = slow_down * 30

all_time = distance_to_clim + slow_down

if all_time >= record_in_seconds:
    print(f"No! He was {all_time - record_in_seconds:.2f} seconds slower.")

elif all_time < record_in_seconds:
    print(f"Yes! The new record is {all_time:.2f} seconds.")

