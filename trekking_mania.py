groups_of_climbers = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0

for i in range(1, groups_of_climbers + 1):
    number_of_climbers = int(input())

    if number_of_climbers <= 5:
        musala += number_of_climbers

    elif 6 <= number_of_climbers <= 12:
        montblanc += number_of_climbers

    elif 13 <= number_of_climbers <= 25:
        kilimanjaro += number_of_climbers

    elif 26 <= number_of_climbers <= 40:
        k2 += number_of_climbers

    else:
        everest += number_of_climbers

total_climbers = musala + montblanc + kilimanjaro + k2 + everest
percentage_musala = musala / total_climbers * 100
percentage_montblanc = montblanc / total_climbers * 100
percentage_kilimanjaro = kilimanjaro / total_climbers * 100
percentage_k2 = k2 / total_climbers * 100
percentage_everest = everest / total_climbers * 100

print(f'{percentage_musala:.2f}%')
print(f'{percentage_montblanc:.2f}%')
print(f'{percentage_kilimanjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everest:.2f}%')


