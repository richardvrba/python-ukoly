print("Je zadané číslo PRVOČÍSLEM?\n")
a = int(input("Zadej celé číslo k testování: "))

je_prvocislo = True

if a < 2:
    je_prvocislo = False
else:
    i = 2
    while i < a:
        if a % i == 0:
            je_prvocislo = False
            break
        i += 1

if je_prvocislo:
    print(f"Číslo {a} JE prvočíslo.")
else:
    print(f"Číslo {a} NENÍ prvočíslo.")

 