day = input()
ticket = 0

if day == "Monday":
    ticket = 12
elif day == "Tuesday":
    ticket = 12
elif day == "Wednesday":
    ticket = 14
elif day == "Thursday":
    ticket = 14
elif day == "Friday":
    ticket = 12
elif day == "Saturday":
    ticket = 16
elif day == "Sunday":
    ticket = 16

print(ticket)