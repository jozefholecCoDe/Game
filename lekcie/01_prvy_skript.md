# Lekcia 01 — Prvý skript: uvítacia obrazovka

**Cieľ:** premenné, `print`, `input`, f-stringy. Výsledok: hra ťa pozdraví menom.

---

## Teória

### Premenná = pomenovaná škatuľa

```python
meno_hrdinu = "Kael"
hp = 30
utok = 5
zije = True
```

Python si typ domyslí sám. Typy, ktoré ťa teraz zaujímajú:

| Typ | Príklad | Na čo v hre |
|-----|---------|-------------|
| `str` (text) | `"Warrior"` | mená, popisy scén |
| `int` (celé číslo) | `30` | HP, útok, XP |
| `float` (desatinné) | `1.5` | multiplikátory kociek |
| `bool` (áno/nie) | `True` | či postava žije |

### Výpis a f-string

```python
print("Ahoj")
print(f"{meno_hrdinu} má {hp} HP")   # f pred úvodzovkami = vkladanie premenných
```

Bez `f` sa `{hp}` vypíše doslova. Toto je najčastejšia chyba začiatočníka.

### Vstup od hráča

```python
odpoved = input("Ako sa voláš? ")
```

⚠️ `input()` **vždy** vráti text. Aj keď hráč napíše `5`, dostaneš `"5"`.
Na číslo to preložíš cez `int(...)`:

```python
vek = int(input("Vek: "))
```

### Komentáre

```python
# toto Python ignoruje, je to pre teba a pre teba o pol roka
```

---

## Ako skript spustíš

V termináli VS Code, z koreňového priečinka projektu:

```
python hra/main.py
```

> **Nepíš zatiaľ `python -m hra`.** Dostaneš hlášku
> `'hra' is a package and cannot be directly executed`. Prepínač `-m` hľadá
> v priečinku súbor `__main__.py` a ten vytvoríš až v lekcii 05. Do tej doby
> spúšťaš súbory priamo cestou.

Ak si zvyknutý na tlačidlo ▶ vpravo hore, funguje tiež — spustí súbor, ktorý
máš práve otvorený. Dôležité je len to, aby výstup šiel do **terminálu**,
inak nebudeš vedieť odpovedať na `input()`.

---

## Úloha

Vytvor `hra/main.py` a naprogramuj uvítaciu obrazovku:

1. Vypíš názov hry v rámčeku z `=` znakov.
2. Spýtaj sa hráča na meno.
3. Ulož do premenných štartovacie hodnoty Warriora: `hp = 30`, `utok = 5`,
   `obrana = 2`, `rage = 0`.
4. Vypíš kartu postavy, napr.:

```
==============================
       SYN KOVÁČA
==============================
Vitaj, Kael.
Trieda: Warrior
❤️  HP:     30
⚔️  Útok:   5
🛡️  Obrana: 2
🔥 Rage:   0
```

### Bonus (skús, nemusíš)

Vypíš aj „silu úderu bez kocky" ako `utok` a s kockou D6 ako `utok + 6`
(zatiaľ napevno, náhodu pridáme v lekcii 11).

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| `SyntaxError: unterminated string` | chýba zatvárajúca úvodzovka |
| vypíše sa `{meno}` doslova | zabudnuté `f` pred úvodzovkami |
| `TypeError: can only concatenate str` | sčítavaš text s číslom — použi f-string |
| `IndentationError` | medzery na začiatku riadku, kde nemajú byť |

## Kontrola

- Prečo `input()` vracia text aj pri čísle?
- Čo urobí `print(f"{2 + 3}")` a čo `print("{2 + 3}")`?

➡️ Ďalej: `02_rozhodovanie_a_slucky.md`
