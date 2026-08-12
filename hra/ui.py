from hra import konstanty
from hra import data_loader

def hlavicka():
    print("==============================")
    print("         Syn Kováča           ")
    print("==============================")

def menu():
    print("1 - Nová hra")
    print("2 - O hre")
    print("3 - Inventar")
    print("4 - Koniec")

def vyber_triedu():
    for cislo, (tid, t) in enumerate(data_loader.TRIEDY.items(), start=1):
        if t['odomknute']:
            print(f"{cislo} - {t['ikona']} {t['nazov']}")
        else:
            print(f"{cislo} - {t['ikona']} {t['nazov']} 🔐")

def zobraz_postavu(postava):
    print(f"Vitaj {postava['meno']}!")
    print(f"Trieda: {postava['trieda']}")
    print(f"❤️  HP:        {postava['hp']}")
    print(f"⚔️  Útok:      {postava['utok']}")
    print(f"🛡️  Obrana:    {postava['obrana']}")
    print(f"🔥 Rage:       {postava['zdroj']}")

def hp_bar(postava):
    plne = postava['hp'] * konstanty.SIRKA_HP_BARU // postava['hp_max']
    bar = ("[" + "█" * plne + "·" * (konstanty.SIRKA_HP_BARU - plne) + f"] {postava['hp']}/{postava['hp_max']}")
    return bar
