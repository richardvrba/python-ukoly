print("Je zadané číslo PRVOČÍSLEM?\n")
n = int(input("Zadej celé číslo k testování: "))

je_prvocislo = True

if n < 2:
    je_prvocislo = False
else:
    i = 2
    while i < n:
        if n % i == 0:
            je_prvocislo = False
            break
        i += 1

if je_prvocislo:
    print(f"Číslo {n} JE prvočíslo.")
else:
    print(f"Číslo {n} NENÍ prvočíslo.")

 