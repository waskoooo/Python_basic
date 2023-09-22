vegetables_price = float(input())
fruits_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

fruits = fruits_price * fruit_kg
vegetables = vegetables_price * vegetable_kg

end_summary = fruits + vegetables

price_in_euro = end_summary / 1.94

print(f"{price_in_euro:.2f}")