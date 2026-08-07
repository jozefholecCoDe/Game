from hra import konstanty

def hlavicka():
    print("==============================")
    print("         Syn Kováča           ")
    print("==============================")

def menu():
    print("1 - Nová hra")
    print("2 - O hre")
    print("3 - Inventar")
    print("4 - Koniec")

def zobraz_postavu(postava):
    print(f"Vitaj {postava['meno']}!")
    print(f"❤️  HP:        {postava['hp']}")
    print(f"⚔️  Útok:      {postava['utok']}")
    print(f"🛡️  Obrana:    {postava['obrana']}")
    print(f"🔥 Rage:       {postava['rage']}")

def hp_bar(postava):
    plne = postava['hp'] * konstanty.SIRKA_HP_BARU // postava['hp_max']
    bar = ("[" + "█" * plne + "·" * (konstanty.SIRKA_HP_BARU - plne) + f"] {postava['hp']}/{postava['hp_max']}")
    print(f"{bar}")

def najsilnejsi_nepriatel(nepriatelia):
    najsilnejsi = ""
    najviac_hp = 0
    for kluc, data in nepriatelia.items():
        if data['hp'] > najviac_hp:
            najviac_hp = data['hp']
            najsilnejsi = kluc
    return najviac_hp, najsilnejsi
