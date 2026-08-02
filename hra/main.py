utok = 5
obrana = 2
rage = 0
kocka = 6

utok_celkom = utok + kocka

trieda = "warrior"

hp = 15
maximum = 30

def hlavicka():
    print("==============================")
    print("         Syn Kováča           ")
    print("==============================")

def menu():
    print("1 - Nová hra")
    print("2 - O hre")
    print("3 - Koniec")

def vytvor_warriora(meno, trieda):
    print(f"Trieda: {trieda}")
    return meno

def zobraz_postavu(hp, utok_celkom, obrana, rage):
    print(f"❤️  HP:        {hp}")
    print(f"⚔️  Útok:      {utok_celkom}")
    print(f"🛡️  Obrana:    {obrana}")
    print(f"🔥 Rage:       {rage}")

def hp_bar(hp, maximum):
    plne = hp * 20 // maximum
    bar = ("[" + "█" * plne + "·" * (20 - plne) + f"] {hp}/{maximum}")
    return bar

def vypocitaj_poskodenie(utok, obrana):
    poskodenie = utok - obrana
    if poskodenie < 1:
        poskodenie = 1
    return poskodenie

def hlavna_slucka():
    hra_bezi = True
    while hra_bezi:
        hlavicka()
        menu()
        volba = input("> ")
        if volba == "1":
            zadaj_meno = input("Zadaj meno: ")
            meno = vytvor_warriora(zadaj_meno, trieda)
            print(f"Vitaj {meno}!")
            zobraz_postavu(hp, utok_celkom, obrana, rage)
            print(hp_bar(hp, maximum))
            poskodenie = vypocitaj_poskodenie(utok_celkom, 0)
            print(f"Spôsobené poškodenie: {poskodenie}")
        elif volba == "2":
            print("Zatial nič")
        elif volba == "3":
            hra_bezi = False
        else:
            print("NEPLATNA VOLBA!!!!!!")

if __name__ == "__main__":
    hlavna_slucka()
