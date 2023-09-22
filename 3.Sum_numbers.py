NUMBER = int(input())

more_numbers = 0

while True:
    current_number = int(input())
    more_numbers += current_number

    if more_numbers >= NUMBER:
        print(more_numbers)
        break