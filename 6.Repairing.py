PLASTIC_BAG = 1.50
PAINT = 14.50
PAINT_LIQUID = 5.00

plastic = int(input())
paint = int(input())
liquid = int(input())
hours_work = int(input())

sum_plastic = (plastic + 2) * PLASTIC_BAG
sum_paint = (paint + (paint * 0.10)) * PAINT
sum_liquid = liquid * PAINT_LIQUID

goods_price = sum_plastic + sum_paint + sum_liquid + 0.40

work_sum = (goods_price * 0.30) * hours_work

end_summary = work_sum + goods_price

print(end_summary)