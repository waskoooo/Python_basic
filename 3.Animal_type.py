animal_type = input()
animal = ""

if animal_type == "dog":
    animal = "mammal"
elif animal_type == "crocodile" or animal_type == "tortoise" or animal_type == "snake":
    animal = "reptile"
else:
    animal = "unknown"

print(animal)