import random
tajne_cislo = random.randint(1, 20)

tip = 0
pokusy = 0

print("Myslím si číslo od 1 do 20. Zkus ho uhodnout!")


while tip!= tajne_cislo:
    tip = int(input("Zadej svůj tip: "))
    pokusy += 1

    if tip < tajne_cislo:
        print("Myslím si větší číslo.")
    elif tip > tajne_cislo:
        print("Myslím si menší číslo.")

print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")