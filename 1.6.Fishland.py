skumriq_price = float(input())
caca_price = float(input())

palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())


palamud = skumriq_price * 1.60
safrid = caca_price * 1.80
midi = 7.50

all_cost = palamud * palamud_kg + safrid * safrid_kg + midi * midi_kg

print(f"{all_cost:.2f}")