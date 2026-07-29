"""Lekcia 02 — hlavné menu v slučke.

if/elif/else, while, for, break.
"""

SIRKA_BARU = 20

# --- postava (zatiaľ ako samostatné premenné, v lekcii 04 to zmeníme) ----
meno_hrdinu = ""
hp = 30
hp_max = 30
utok = 5
obrana = 2
rage = 0

print("=" * 30)
print("       SYN KOVÁČA")
print("=" * 30)

bezi = True
while bezi:
    print()
    print("1) Nová hra")
    print("2) O hre")
    print("3) Koniec")

    volba = input("> ").strip()

    if volba == "1":
        meno_hrdinu = input("Ako sa voláš, hrdina? ").strip()
        if meno_hrdinu == "":
            meno_hrdinu = "Bezmenný"

        # HP bar z textu: koľko políčok je plných
        plne = hp * SIRKA_BARU // hp_max
        bar = "█" * plne + "·" * (SIRKA_BARU - plne)

        print()
        print(f"Vitaj, {meno_hrdinu}.")
        print("Trieda: Warrior")
        print(f"❤️  [{bar}] {hp}/{hp_max}")
        print(f"⚔️  Útok:   {utok}")
        print(f"🛡️  Obrana: {obrana}")
        print(f"🔥 Rage:   {rage}")

    elif volba == "2":
        print()
        print("Textové RPG o synovi kováča, ktorý hľadá otcov ukradnutý meč.")
        print("Ťahové súboje, kocky ako predmety, vetvený príbeh.")

    elif volba == "3":
        print("Vyhňa vychladla. Dovidenia.")
        bezi = False

    else:
        print("Neplatná voľba, skús znova.")
