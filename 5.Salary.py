FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50


opened_tabs = int(input())
salary = float(input())

for _ in range(opened_tabs):
    current_opened_tabs = input()

    if current_opened_tabs == "Facebook":
        salary -= FACEBOOK_FINE
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif current_opened_tabs == "Instagram":
        salary -= INSTAGRAM_FINE
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif current_opened_tabs == "Reddit":
        salary -= REDDIT_FINE
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(f"{int(salary)}")