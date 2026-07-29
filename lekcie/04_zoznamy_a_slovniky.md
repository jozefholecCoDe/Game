# Lekcia 04 — Zoznamy a slovníky: postava ako dáta

**Cieľ:** `list`, `dict`. Výsledok: postava nie je 8 premenných, ale jedna vec.

---

## Teória

### Zoznam (`list`) — usporiadaná rada

```python
inventar = ["Kováčske kladivo", "Chlieb", "D6"]

inventar.append("Kožená vesta")   # pridaj na koniec
inventar.remove("Chlieb")         # odstráň podľa hodnoty
print(inventar[0])                # prvý prvok — číslujeme od 0!
print(len(inventar))              # počet prvkov
print("D6" in inventar)           # True / False
```

Prechod zoznamom s číslovaním:

```python
for cislo, predmet in enumerate(inventar, start=1):
    print(f"{cislo}) {predmet}")
```

Toto je presne to, čo potrebuješ na výpis inventára a na výpis volieb v scéne.

### Slovník (`dict`) — dvojice kľúč → hodnota

```python
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

print(postava["hp"])              # 30
postava["hp"] -= 7                # ubli sme 7 HP
postava["xp"] = postava["xp"] + 10
```

### `.get()` — bezpečné čítanie

```python
postava["mana"]              # ❌ KeyError, hra spadne
postava.get("mana")          # ✅ None
postava.get("mana", 0)       # ✅ 0 — predvolená hodnota
```

Pri data-driven dizajne budeš `.get()` používať neustále: nie každá scéna má
`efekty`, nie každý predmet má `kocka`.

### Vnorené dáta — takto bude vyzerať tvoj príbeh

```python
scena = {
    "id": "les_tiene",
    "text": "Pri okraji lesa sa mihne tieň.",
    "volby": [
        {"text": "Vytiahni kladivo", "vedie_na": "boj_vlk"},
        {"text": "Ustúp k dedine", "vedie_na": "dedina", "efekty": {"xp": 5}},
    ],
}

for volba in scena["volby"]:
    print(volba["text"])

print(scena["volby"][0]["vedie_na"])    # "boj_vlk"
```

Čítaj to zvnútra von: `scena` → kľúč `volby` (zoznam) → prvý prvok (slovník)
→ kľúč `vedie_na`.

### Pozor: slovník sa mení „na mieste"

```python
def zran(postava, kolko):
    postava["hp"] -= kolko      # zmena je viditeľná aj vonku

zran(postava, 5)
print(postava["hp"])            # naozaj sa zmenilo
```

Toto je iné než pri číslach z lekcie 03 a je to zámerné — takto budeš meniť
stav postavy počas boja. Ale platí: funkcia, ktorá **mení** stav, nech ho
nemení potajomky. Nazvi ju tak, aby to bolo zjavné (`zran`, `pridaj_xp`).

---

## Úloha

1. Nahraď jednotlivé premenné jedným slovníkom `postava`.
2. Uprav funkcie z lekcie 03, aby brali `postava` ako parameter:
   ```python
   def zobraz_postavu(postava): ...
   def zran(postava, kolko): ...
   def pridaj_do_inventara(postava, predmet): ...
   ```
3. Vytvor slovník `NEPRIATELIA` s aspoň troma nepriateľmi:
   ```python
   NEPRIATELIA = {
       "vlk":     {"meno": "Hladný vlk",  "hp": 12, "utok": 4, "obrana": 0, "xp": 10},
       "zbojnik": {"meno": "Zbojník",     "hp": 18, "utok": 5, "obrana": 1, "xp": 15},
       "grimjaw": {"meno": "Grimjaw",     "hp": 34, "utok": 8, "obrana": 3, "xp": 40},
   }
   ```
4. Do menu pridaj položku „Inventár", ktorá vypíše očíslovaný zoznam.
5. Napíš funkciu `najsilnejsi_nepriatel(nepriatelia)`, ktorá vráti meno toho
   s najvyšším HP. (Nápoveda: prejdi `.items()` a pamätaj si maximum.)

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| `KeyError: 'mana'` | kľúč neexistuje — použi `.get()` |
| `IndexError: list index out of range` | siahaš na `[3]` v troch prvkoch (indexy 0,1,2) |
| `TypeError: unhashable type: 'list'` | zoznam ako kľúč slovníka — nejde |
| dva „rôzne" slovníky sa menia naraz | priradil si `b = a`, čo je ten istý objekt; použi `a.copy()` |

## Kontrola

- Kedy zoznam a kedy slovník?
- Čo vráti `postava.get("stit", "žiadny")`, ak kľúč neexistuje?
- Ako sa dostaneš k textu druhej voľby v ukážke `scena`?

➡️ Ďalej: `05_moduly_a_struktura.md`
