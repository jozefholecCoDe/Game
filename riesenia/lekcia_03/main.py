"""Lekcia 03 — to isté menu, ale rozdelené na funkcie.

Všimni si rozdelenie zodpovedností:
  - funkcie, ktoré POČÍTAJÚ, vracajú hodnotu a nikdy nevolajú print
    (vypocitaj_poskodenie, hp_bar, vytvor_warriora)
  - funkcie, ktoré ZOBRAZUJÚ, volajú print a nič nevracajú
    (zobraz_hlavicku, zobraz_menu, zobraz_postavu)

Toto pravidlo ti v lekcii 17 umožní napísať testy a v lekcii 24 pridať
grafiku bez prepisovania logiky.
"""

SIRKA_BARU = 20
MIN_POSKODENIE = 1


# --- výpočty (bez print) --------------------------------------------------

def vytvor_warriora(meno):
    """Vráti štartovacie hodnoty Warriora ako niekoľko hodnôt naraz."""
    return meno, 30, 30, 5, 2, 0


def hp_bar(hp, maximum, sirka=SIRKA_BARU):
    """Vráti textový HP bar. Nevypisuje ho — to je práca UI."""
    if maximum <= 0:
        return "·" * sirka
    plne = hp * sirka // maximum
    plne = max(0, min(sirka, plne))
    return "█" * plne + "·" * (sirka - plne)


def vypocitaj_poskodenie(utok, obrana):
    """Vráti poškodenie po odpočítaní obrany, vždy aspoň MIN_POSKODENIE."""
    return max(MIN_POSKODENIE, utok - obrana)


# --- zobrazenie (tu a len tu sa printuje) ---------------------------------

def zobraz_hlavicku():
    print("=" * 30)
    print("       SYN KOVÁČA")
    print("=" * 30)


def zobraz_menu():
    print()
    print("1) Nová hra")
    print("2) O hre")
    print("3) Koniec")


def zobraz_postavu(meno, hp, hp_max, utok, obrana, rage):
    print()
    print(f"Vitaj, {meno}.")
    print("Trieda: Warrior")
    print(f"❤️  [{hp_bar(hp, hp_max)}] {hp}/{hp_max}")
    print(f"⚔️  Útok:   {utok}")
    print(f"🛡️  Obrana: {obrana}")
    print(f"🔥 Rage:   {rage}")


def zobraz_o_hre():
    print()
    print("Textové RPG o synovi kováča, ktorý hľadá otcov ukradnutý meč.")
    print("Ťahové súboje, kocky ako predmety, vetvený príbeh.")


# --- riadenie -------------------------------------------------------------

def nova_hra():
    meno = input("Ako sa voláš, hrdina? ").strip() or "Bezmenný"
    meno, hp, hp_max, utok, obrana, rage = vytvor_warriora(meno)
    zobraz_postavu(meno, hp, hp_max, utok, obrana, rage)

    # ukážka výpočtu poškodenia proti vlkovi (obrana 0)
    print(f"\nTvoj úder by vlkovi ubral {vypocitaj_poskodenie(utok, 0)} HP.")


def hlavna_slucka():
    zobraz_hlavicku()
    while True:
        zobraz_menu()
        volba = input("> ").strip()

        if volba == "1":
            nova_hra()
        elif volba == "2":
            zobraz_o_hre()
        elif volba == "3":
            print("Vyhňa vychladla. Dovidenia.")
            break
        else:
            print("Neplatná voľba, skús znova.")


if __name__ == "__main__":
    hlavna_slucka()
