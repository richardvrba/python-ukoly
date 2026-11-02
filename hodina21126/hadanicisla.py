import random
tajne_cislo = random.randint(1, 20)

tip = 0
pokusy = 0
max_pokusu = 5

print(f"Myslím si číslo od 1 do 20. Zkus ho uhodnout, máš na to {max_pokusu} pokusů!")


while tip!= tajne_cislo:
    tip = int(input("Zadej svůj tip: "))
    pokusy += 1

    if tip < tajne_cislo:
        print("Myslím si větší číslo.")
    elif tip > tajne_cislo:
        print("Myslím si menší číslo.")

if tip == tajne_cislo:
    print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
else:
    print(f"Bohužel, neuhodl jsi číslo {tajne_cislo}. Měl jsi {max_pokusu} pokusů.")