import random

tajne_cislo = random.randint(1, 20)
pokusy = 0
max_pokusu = 5

print(f"Myslím si číslo od 1 do 20. Zkus ho uhodnout, máš na to {max_pokusu} pokusů!")

while pokusy < max_pokusu:
    tip = int(input("Zadej svůj tip: "))
    pokusy += 1

    if tip == tajne_cislo:
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
        break
    elif tip < tajne_cislo:
        print("Myslím si větší číslo.")
    else:
        print("Myslím si menší číslo.")

    if pokusy == max_pokusu and tip != tajne_cislo:
        print(f"Bohužel, došly ti pokusy. Myslel jsem si číslo {tajne_cislo}.")