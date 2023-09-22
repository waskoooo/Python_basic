some_string = input()
char = 0

for word in some_string:
    if word == "a":
        char += 1
    elif word == "e":
        char += 2
    elif word == "i":
        char += 3
    elif word == "o":
        char += 4
    elif word == "u":
        char += 5

print(char)