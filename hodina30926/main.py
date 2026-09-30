print("Kalkulačka spropitného")
celkova_cena = float(input("Zadejte celkovou cenu: "))
spropitne = int(input("Zadej spropitné v %: "))
pocet_lidi = int(input("Zadej počet lidí: "))

celkova_cena += celkova_cena * spropitne / 100
print (celkova_cena)

uhradit = round(celkova_cena / pocet_lidi)
print(uhradit)

print(f"Celková cena {celkova_cena} dělená {pocet_lidi} je {uhradit+5} Kč")