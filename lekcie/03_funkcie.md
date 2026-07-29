# Lekcia 03 — Funkcie: upratovanie menu

**Cieľ:** `def`, parametre, `return`, rozsah premenných. Výsledok: `main.py`,
ktorý sa dá čítať.

---

## Teória

### Funkcia = pomenovaný kus kódu

```python
def pozdrav(meno):
    print(f"Vitaj, {meno}.")

pozdrav("Kael")
```

### `return` — funkcia, ktorá niečo vráti

```python
def vypocitaj_poskodenie(utok, obrana):
    poskodenie = utok - obrana
    if poskodenie < 1:
        poskodenie = 1          # vždy aspoň 1 bod
    return poskodenie

zranenie = vypocitaj_poskodenie(5, 2)   # 3
```

**Zapamätaj si tento rozdiel — je to najdôležitejšia vec v lekcii:**

- Funkcia, ktorá **počíta**, používa `return` a **nikdy nevolá `print`**.
- Funkcia, ktorá **zobrazuje**, volá `print` a **nič nevracia**.

Toto je pravidlo č. 2 z `UCEBNY_PLAN.md`. Vďaka nemu neskôr pridáš grafiku
bez toho, aby si prepisoval súbojový systém.

### Predvolené a pomenované parametre

```python
def hod_kockou(stien=6, pocet=1):
    ...

hod_kockou()             # D6
hod_kockou(20)           # D20
hod_kockou(stien=3)      # D3, čitateľnejšie
```

### Rozsah premenných (scope)

```python
hp = 30

def uber_hp():
    hp = 10        # ❌ vytvorí NOVÚ lokálnu premennú, vonkajšiu nezmení

def uber_hp_spravne(aktualne_hp, kolko):
    return aktualne_hp - kolko     # ✅ vezmi vstup, vráť výstup
```

Nepoužívaj `global`. Ak sa ti zdá, že ho potrebuješ, funkcii chýba parameter.

### Docstring

```python
def vypocitaj_poskodenie(utok, obrana):
    """Vráti poškodenie po odpočítaní obrany, minimálne 1."""
```

---

## Úloha

Prerob `hra/main.py` na funkcie. Cieľ: v hlavnej slučke nesmie byť žiadny
výpočet, len volania funkcií.

Navrhované funkcie:

```python
def zobraz_hlavicku():          ...   # rámček s názvom hry
def zobraz_menu():              ...   # výpis možností
def vytvor_warriora(meno):      ...   # vráti postavu (zatiaľ ako niekoľko hodnôt)
def zobraz_postavu(...):        ...   # karta postavy
def hp_bar(hp, maximum):        ...   # VRÁTI text baru, nevypisuje ho!
def vypocitaj_poskodenie(utok, obrana): ...
def hlavna_slucka():            ...   # while + if/elif
```

Na konci súboru:

```python
if __name__ == "__main__":
    hlavna_slucka()
```

(Čo presne robí `__name__`, vysvetlíme v lekcii 05. Zatiaľ ber ako „toto sa
spustí, keď súbor spustíš priamo".)

### Kontrolná otázka k úlohe

Prečo má `hp_bar()` vracať text namiesto toho, aby ho rovno vypísala?
Ak nevieš odpovedať, vráť sa na sekciu o `return`.

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| funkcia vráti `None` | zabudnutý `return` |
| `NameError` | funkcia definovaná až pod miestom volania... alebo preklep |
| zmena v funkcii sa „neprejaví" | menil si lokálnu kópiu, chýba `return` |

## Kontrola

- Aký je rozdiel medzi `print(x)` a `return x`?
- Čo vráti funkcia bez `return`?
- Prečo je `global` zlý nápad?

➡️ Ďalej: `04_zoznamy_a_slovniky.md`
