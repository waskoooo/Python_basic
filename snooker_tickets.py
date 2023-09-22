competition_stage = input()
type_ticket = input()
ticket_count = int(input())
trophy_picture = input()

ticket_price = 0
pictures = 40
picture_price = 0


if competition_stage == "Quarter final":
    if type_ticket == "Standard":
        ticket_price = 55.50
    elif type_ticket == "Premium":
        ticket_price = 105.20
    elif type_ticket == "VIP":
        ticket_price = 118.90
elif competition_stage == "Semi final":
    if type_ticket == "Standard":
        ticket_price = 75.88
    elif type_ticket == "Premium":
        ticket_price = 125.22
    elif type_ticket == "VIP":
        ticket_price = 300.40
elif competition_stage == "Final":
    if type_ticket == "Standard":
        ticket_price = 110.10
    elif type_ticket == "Premium":
        ticket_price = 160.66
    elif type_ticket == "VIP":
        ticket_price = 400

tickets_cost = ticket_price * ticket_count

if tickets_cost > 4000:
    tickets_cost = tickets_cost * 0.75
elif tickets_cost > 2500:
    tickets_cost = tickets_cost * 0.90

if trophy_picture == "Y" and tickets_cost < 4000:
    picture_price = pictures * ticket_count
elif trophy_picture == "N":
    picture_price = 0

print(f"{tickets_cost + picture_price:.2f}")

