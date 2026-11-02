pocitadlo = 50

while pocitadlo > 0:
    print(f"Číslo: {pocitadlo}")
    pocitadlo -= 10

while pocitadlo <= 5:
    print(f"Číslo: {pocitadlo}")
    if pocitadlo == 30:
        break

print("Konec cyklu")
print(f"Číslo: {pocitadlo}")