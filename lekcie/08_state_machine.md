# Lekcia 08 — State machine obrazoviek

**Cieľ:** `Enum`, slovník funkcií. Výsledok: prepínanie obrazoviek bez
tisícriadkového `if`.

---

## Problém

Bez state machine skončíš takto:

```python
while True:
    if obrazovka == "menu":
        ...50 riadkov...
    elif obrazovka == "vyber_postavy":
        ...40 riadkov...
    elif obrazovka == "suboj":
        ...200 riadkov...
```

Po piatich obrazovkách sa v tom nevyznáš.

## Teória

### `Enum` — pomenované konštanty

```python
from enum import Enum, auto

class Stav(Enum):
    MENU = auto()
    VYBER_POSTAVY = auto()
    PRIBEH = auto()
    SUBOJ = auto()
    INVENTAR = auto()
    KNIHA_KUZIEL = auto()
    LEVEL_UP = auto()
    KONIEC = auto()
```

Prečo nie obyčajný text? Lebo `Stav.SUBOJJ` spadne hneď, kým `"subojj"`
sa ticho prepadne do `else`.

### Vzor: každá obrazovka je funkcia, ktorá vráti ďalší stav

```python
def obrazovka_menu(hra):
    """Vykreslí menu, spracuje vstup, vráti nasledujúci stav."""
    ui.zobraz_menu()
    volba = input("> ").strip()
    if volba == "1":
        return Stav.VYBER_POSTAVY
    if volba == "2":
        return Stav.NACITANIE
    if volba == "3":
        return Stav.KONIEC
    ui.chyba("Neplatná voľba.")
    return Stav.MENU        # zostaň, kde si
```

### Hlavná slučka — a je hotovo

```python
OBRAZOVKY = {
    Stav.MENU: obrazovka_menu,
    Stav.VYBER_POSTAVY: obrazovka_vyber_postavy,
    Stav.PRIBEH: obrazovka_pribeh,
    Stav.SUBOJ: obrazovka_suboj,
}

def spusti():
    hra = Hra()
    stav = Stav.MENU
    while stav is not Stav.KONIEC:
        obrazovka = OBRAZOVKY[stav]
        stav = obrazovka(hra)
    print("Ďakujeme za hru.")
```

Táto slučka sa už **nikdy nezmení**, aj keď pridáš dvadsať obrazoviek.
Pridávanie obrazovky = nová funkcia + riadok v slovníku.

### Kam s dátami? Objekt `Hra`

```python
class Hra:
    """Všetko, čo prežíva medzi obrazovkami."""
    def __init__(self):
        self.postava = None
        self.aktualna_scena = "uvod"
        self.aktualny_suboj = None
        self.predch_stav = None      # kam sa vrátiť z inventára
```

Obrazovky si podávajú tento jeden objekt. Žiadne globálne premenné.

### Návrat z inventára

Inventár sa dá otvoriť z príbehu aj zo súboja. Preto:

```python
def obrazovka_inventar(hra):
    ...
    return hra.predch_stav      # vráť sa tam, odkiaľ si prišiel
```

A ten, kto inventár otvára, si predtým nastaví `hra.predch_stav = Stav.PRIBEH`.

---

## Úloha

1. Vytvor `hra/stavy.py` s `Enum` `Stav`.
2. Vytvor `hra/obrazovky.py`, kde bude každá obrazovka ako funkcia
   `obrazovka_xxx(hra) -> Stav`.
3. Presuň hlavnú slučku do `hra/main.py` a sprav ju **prázdnu** — len
   vyhľadanie funkcie v slovníku a volanie.
4. Sprav funkčné: `MENU`, `VYBER_POSTAVY`, `INVENTAR`, `KONIEC`.
   `PRIBEH` a `SUBOJ` nech zatiaľ len vypíšu „TODO" a vrátia sa do menu.
5. Implementuj návrat z inventára cez `hra.predch_stav`.

### Kontrolná otázka k úlohe

Koľko riadkov v `main.py` musíš zmeniť, aby si pridal obrazovku
„Nastavenia"? Ak viac než jeden, slovník `OBRAZOVKY` nie je na správnom mieste.

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| `KeyError: <Stav.SUBOJ>` | stav nie je v slovníku `OBRAZOVKY` |
| slučka sa zacyklí na jednej obrazovke | funkcia zabudla `return` — vráti `None` |
| `TypeError: 'NoneType' object is not callable` | to isté, `None` sa hľadá v slovníku |

## Kontrola

- Prečo `Enum` a nie text?
- Prečo obrazovka **vracia** ďalší stav, namiesto aby ho nastavovala sama?
- Načo slúži objekt `Hra`?

➡️ Ďalej: `09_pribehovy_engine.md`
