bitcoin = 1168
chineese_uan = 0.15         #dollars
dollar = 1.76
euro = 1.95

count_bitcoin = int(input())
count_chinnese = float(input())
commission = float(input()) # / 100
commission_precentige = commission / 100

chineese_uan_lv = chineese_uan * dollar

price = bitcoin * count_bitcoin + count_chinnese * chineese_uan_lv

price_in_euro = price / euro

bureau_commisiion = price_in_euro * commission_precentige

final_price = price_in_euro - bureau_commisiion

print(f"{final_price:.2f}")

