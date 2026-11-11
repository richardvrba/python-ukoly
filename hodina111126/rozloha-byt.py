def spocitej_obsah(a, b):
    if a<= 0 or b<= 0:
        return None
    obsah = a * b
    return obsah

print("VÝPOČET ROZLOHY BYTU")
pocet_mistnosti = int(input("Zadejte počet místností: "))
mistnost = 1
while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost}. místnosti: ")
    a = int(input("Zadejte rozměr \"a\": "))
    b = int(input("Zadejte rozměr \"b\": "))
    obsah_mistnosti = spocitej_obsah(a, b)
    if obsah_mistnosti is None:
        obsah += obsah_mistnosti
        mistnost += 1
print(f"Celková rozloha bytu je {obsah} m²")