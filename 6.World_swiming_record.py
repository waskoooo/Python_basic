record_in_seconds = float(input())
lent_in_m = float(input())
time_sec__min = float(input())

must_swim = lent_in_m * time_sec__min
water_pressure = (lent_in_m // 15) * 12.5
all_time = must_swim + water_pressure



if record_in_seconds <= all_time:
    print(f'No, he failed! He was {all_time - record_in_seconds:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {all_time:.2f} seconds.')