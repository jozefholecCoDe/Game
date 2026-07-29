"""Lekcia 01 — uvítacia obrazovka.

Premenné, print, input, f-stringy.
"""

# --- uvítanie -------------------------------------------------------------
print("=" * 30)
print("       SYN KOVÁČA")
print("=" * 30)

meno_hrdinu = input("Ako sa voláš, hrdina? ").strip()

# Ak hráč nič nenapíše, dáme mu meno sami.
if meno_hrdinu == "":
    meno_hrdinu = "Bezmenný"

# --- štartovacie hodnoty Warriora ----------------------------------------
trieda = "Warrior"
hp = 30
hp_max = 30
utok = 5
obrana = 2
rage = 0

# --- karta postavy --------------------------------------------------------
print()
print(f"Vitaj, {meno_hrdinu}.")
print(f"Trieda: {trieda}")
print(f"❤️  HP:     {hp}/{hp_max}")
print(f"⚔️  Útok:   {utok}")
print(f"🛡️  Obrana: {obrana}")
print(f"🔥 Rage:   {rage}")

# --- bonus: sila úderu ----------------------------------------------------
kocka_stien = 6
print()
print(f"Úder bez kocky:   {utok}")
print(f"Úder s D{kocka_stien} (max): {utok + kocka_stien}")
