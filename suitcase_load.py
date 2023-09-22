airplane_capacity = float(input())
counter = 0
command = input()

while command != "End":
    suitcase = float(command)

    if (counter + 1) % 3 == 0:
        suitcase *= 1.1
    if suitcase > airplane_capacity:
        print("No more space!")
        print(f'Statistic: {counter} suitcases loaded.')
        break

    airplane_capacity -= suitcase
    counter += 1
    command = input()
if command == "End":
    print("Congratulations! All suitcases are loaded!")
    print(f'Statistic: {counter} suitcases loaded.')
