upper_limit_first = int(input())
upper_limit_second = int(input())
upper_limit_third = int(input())

for first in range(2, upper_limit_first + 1, 2):
    for second in range(2, upper_limit_second + 1):
        is_second_prime = True
        for i in range(2, second):
            if second % i == 0:
                is_second_prime = False
                break
        if is_second_prime:
            for third in range(2, upper_limit_third + 1, 2):
                print(f"{first} {second} {third}")
