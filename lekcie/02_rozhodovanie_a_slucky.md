# Lekcia 02 — Rozhodovanie a slučky: hlavné menu

**Cieľ:** `if/elif/else`, `while`, `for`. Výsledok: menu, ktoré beží dokola,
kým hráč nezvolí „Koniec".

---

## Teória

### Podmienky

```python
if hp <= 0:
    print("Padol si.")
elif hp < 10:
    print("Krvácaš.")
else:
    print("Držíš sa.")
```

**Odsadenie je syntax.** Python nemá `{}` — telo bloku určujú 4 medzery.
Nikdy nemiešaj tabulátory a medzery.

### Porovnávanie a logika

```python
==  !=  <  >  <=  >=
and   or   not
```

```python
if hp > 0 and rage >= 3:
    print("Môžeš použiť kúzlo.")
```

⚠️ `=` priraďuje, `==` porovnáva. Zámena je klasická chyba.

### Slučka `while` — kým platí podmienka

```python
bezi = True
while bezi:
    volba = input("> ")
    if volba == "3":
        bezi = False
```

Toto je zárodok tvojej **hernej slučky**. Každá hra na svete je while slučka.

### Slučka `for` — pre každý prvok

```python
for i in range(3):
    print(i)        # 0, 1, 2

for pismeno in "HP":
    print(pismeno)  # H, P
```

### `break` a `continue`

```python
while True:
    volba = input("> ")
    if volba == "koniec":
        break        # okamžite von zo slučky
    if volba == "":
        continue     # preskoč zvyšok, choď na ďalšie kolo
    print(f"Zvolil si {volba}")
```

---

## Úloha

Rozšír `hra/main.py`:

1. Po uvítaní zobraz menu:
   ```
   1) Nová hra
   2) O hre
   3) Koniec
   ```
2. Načítaj voľbu a spracuj ju cez `if/elif/else`.
3. Zabaľ to do `while` slučky, aby sa menu vrátilo po každej akcii.
4. Pri neplatnej voľbe vypíš `Neplatná voľba, skús znova.` a **nespadni**.
5. „Nová hra" zatiaľ len vypíše kartu postavy z lekcie 01.

### Bonus

Sprav jednoduchý „HP bar" z textu:

```python
hp = 21
maximum = 30
plne = hp * 20 // maximum          # // je celočíselné delenie
print("[" + "█" * plne + "·" * (20 - plne) + f"] {hp}/{maximum}")
```

Vyskúšaj rôzne hodnoty `hp` a pochop, prečo tam je `//` a nie `/`.

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| nekonečná slučka | podmienka `while` sa nikdy nezmení na `False` |
| `IndentationError` | nekonzistentné odsadenie |
| menu vždy padne do `else` | porovnávaš `volba == 1` (číslo) s textom `"1"` |

## Kontrola

- Kedy použiješ `while` a kedy `for`?
- Aký je rozdiel medzi `break` a `continue`?
- Prečo `input()` porovnávaš s `"1"` a nie s `1`?

➡️ Ďalej: `03_funkcie.md`
