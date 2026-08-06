postava = {
    "meno": "Kael",
    "trieda": "warrior",
    "hp": 30,
    "hp_max": 30,
    "utok": 5,
    "obrana": 2,
    "rage": 0,
    "level": 1,
    "xp": 0,
    "inventar": ["D6"],
}

NEPRIATELIA = {
    "vlk":     {"meno": "Hladný vlk",  "hp": 12, "utok": 4, "obrana": 0, "xp": 10},
    "zbojnik": {"meno": "Zbojník",     "hp": 18, "utok": 5, "obrana": 1, "xp": 15},
    "grimjaw": {"meno": "Grimjaw",     "hp": 34, "utok": 8, "obrana": 3, "xp": 40},
}

def hlavicka():
    print("==============================")
    print("         Syn Kováča           ")
    print("==============================")

def menu():
    print("1 - Nová hra")
    print("2 - O hre")
    print("3 - Inventar")
    print("4 - Koniec")

def vytvor_warriora(postava):
    print(f"Trieda: {postava['trieda']}")
    return postava['meno']

def zobraz_postavu(postava):
    print(f"❤️  HP:        {postava['hp']}")
    print(f"⚔️  Útok:      {postava['utok']}")
    print(f"🛡️  Obrana:    {postava['obrana']}")
    print(f"🔥 Rage:       {postava['rage']}")

def hp_bar(postava):
    plne = postava['hp'] * 20 // postava['hp_max']
    bar = ("[" + "█" * plne + "·" * (20 - plne) + f"] {postava['hp']}/{postava['hp_max']}")
    return bar

def vypocitaj_poskodenie(utok, obrana):
    poskodenie = utok - obrana
    if poskodenie < 1:
        poskodenie = 1
    return poskodenie

def zran(ciel, kolko):
    ubrane = min(kolko, ciel['hp'])
    ciel['hp'] -= ubrane
    return ubrane

def pridaj_do_inventara(postava, predmet):
    postava['inventar'].append(predmet)

def najsilnejsi_nepriatel(nepriatelia):
    najsilnejsi = ""
    najviac_hp = 0
    for kluc, data in nepriatelia.items():
        if data['hp'] > najviac_hp:
            najviac_hp = data['hp']
            najsilnejsi = kluc
    return najviac_hp, najsilnejsi



def hlavna_slucka():
    hra_bezi = True
    while hra_bezi:
        hlavicka()
        menu()
        volba = input("> ")
        if volba == "1":
            postava['meno'] = input("Zadaj meno: ")
            meno = vytvor_warriora(postava)
            print(f"Vitaj {meno}!")
            zobraz_postavu(postava)
            print(hp_bar(postava))
            poskodenie = vypocitaj_poskodenie(NEPRIATELIA ['vlk']['utok'], postava['obrana'])
            print(postava['hp'])
            aktualne = zran(postava, poskodenie)
            print(f"Spôsobené poškodenie VLKOM: {aktualne}")
            print(postava['hp'])
            print("Ziskal si predmet: Kladivo")
            pridaj_do_inventara(postava, "kladivo")
            print(postava['inventar'])
            print(najsilnejsi_nepriatel(NEPRIATELIA))
        elif volba == "2":
            print("Zatial nič")
        elif volba == "3":
            print(postava['inventar'])
        elif volba == "4":
            hra_bezi = False
        else:
            print("NEPLATNA VOLBA!!!!!!")

if __name__ == "__main__":
    hlavna_slucka()
