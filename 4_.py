def main():
    n = int(input())  # Въвеждаме броя на компютрите
    total_sales = 0
    total_rating = 0

    for _ in range(n):  # Итерираме през всички компютри
        computer_data = int(input())  # Въвеждаме данните за текущия компютър
        rating = computer_data % 10  # Изолираме последната цифра - рейтинга
        sales = computer_data // 10  # Останалите цифри са продажбите

        # Изчисляваме продажбите в зависимост от рейтинга
        if rating == 2:
            total_sales += 0  # Няма продажби при рейтинг 2
        elif rating == 3:
            total_sales += 0.5 * sales  # Продажбите са 50% от възможните при рейтинг 3
        elif rating == 4:
            total_sales += 0.7 * sales  # Продажбите са 70% от възможните при рейтинг 4
        elif rating == 5:
            total_sales += 0.85 * sales  # Продажбите са 85% от възможните при рейтинг 5
        elif rating == 6:
            total_sales += sales  # Продажбите са 100% от възможните при рейтинг 6

        total_rating += rating  # Сумираме рейтингите за средноаритметичния рейтинг

    average_sales = total_sales / n  # Пресмятаме средноаритметичния брой продажби
    average_rating = total_rating / n  # Пресмятаме средноаритметичния рейтинг

    print(f"{total_sales:.2f}")  # Отпечатваме общите продажби с точност до две десетични знака
    print(f"{average_rating:.2f}")  # Отпечатваме средноаритметичния рейтинг с точност до две десетични знака

if __name__ == "__main__":
    main()
