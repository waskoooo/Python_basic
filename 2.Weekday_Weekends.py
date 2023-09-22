day_of_week = input()
day_print = ""

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    day_print = "Working day"
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    day_print = "Weekend"
else:
    day_print = "Error"

print(day_print)