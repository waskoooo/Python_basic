days_stay = int(input())
type_room = input()
review = input()
nights = days_stay - 1

room_cost = 0

if nights < 10:
    if type_room == 'room for one person':
        room_cost = 18.00
    elif type_room == 'apartment':
        room_cost = 25.00 * 0.70
    elif type_room == 'president apartment':
        room_cost = 35.00 * 0.90

elif 10 <= nights <= 15:
    if type_room == 'room for one person':
        room_cost = 18.00
    elif type_room == 'apartment':
        room_cost = 25.00 * 0.65
    elif type_room == 'president apartment':
        room_cost = 35.00 * 0.85

elif nights > 15:
    if type_room == 'room for one person':
        room_cost = 18.00
    elif type_room == 'apartment':
        room_cost = 25.00 * 0.50
    elif type_room == 'president apartment':
        room_cost = 35.00 * 0.80

if review == 'positive':
    room_cost = room_cost * 1.25
elif review == 'negative':
    room_cost = room_cost * 0.90

print(f'{room_cost * nights:.2f}')
