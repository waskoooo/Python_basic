hour = int(input())
minute = int(input()) + 15

if minute > 59:
    hour += 1
    minute -= 60
if hour > 23:
    hour = 0

print(f'{hour}:{minute:02d}')
