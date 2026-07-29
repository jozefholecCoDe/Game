# Lekcia 05 — Moduly a štruktúra projektu

**Cieľ:** rozbiť jeden veľký súbor na balík. Výsledok: `python3 -m hra` beží.

---

## Teória

### Modul = jeden `.py` súbor

```python
# hra/suboj.py
def vypocitaj_poskodenie(utok, obrana):
    return max(1, utok - obrana)
```

```python
# hra/main.py
from hra.suboj import vypocitaj_poskodenie

zranenie = vypocitaj_poskodenie(5, 2)
```

### Balík = priečinok so súborom `__init__.py`

```
hra/
├── __init__.py      # môže byť prázdny — hovorí „toto je balík"
├── __main__.py      # spustí sa pri `python3 -m hra`
├── main.py
├── postava.py
└── suboj.py
```

### `if __name__ == "__main__"`

Keď súbor **spustíš**, Python doňho nastaví `__name__ = "__main__"`.
Keď ho **importuješ**, `__name__` je meno modulu. Preto:

```python
if __name__ == "__main__":
    hlavna_slucka()      # spustí sa len pri priamom spustení, nie pri importe
```

Bez toho by ti import `main.py` rovno rozbehol celú hru.

### Kruhový import — na čo si dať pozor

Ak `suboj.py` importuje `postava.py` a `postava.py` importuje `suboj.py`,
Python spadne. Riešenie: **dáta a základné typy dole, logika hore.**
Šípky importov nech vedú jedným smerom:

```
main  →  obrazovky  →  suboj  →  postava  →  (nič)
```

---

## Úloha

Rozdeľ doterajší kód na:

| Súbor | Obsah |
|-------|-------|
| `hra/__init__.py` | prázdny |
| `hra/__main__.py` | `from hra.main import hlavna_slucka` + spustenie |
| `hra/main.py` | hlavná slučka a menu |
| `hra/postava.py` | vytvorenie postavy, `zran`, `pridaj_xp`, inventár |
| `hra/suboj.py` | `vypocitaj_poskodenie` a neskôr celý boj |
| `hra/ui.py` | všetko, čo `print`-uje: `hp_bar`, `zobraz_postavu`, `zobraz_menu` |

Otestuj:

```bash
python3 -m hra
```

**Dôležité:** pri presúvaní kódu skontroluj, či `ui.py` naozaj obsahuje
*všetky* `print`-y a ostatné moduly ani jeden. Ak nájdeš `print` v `suboj.py`,
prerob funkciu tak, aby text **vracala**.

### Bonus

Vytvor `hra/konstanty.py` s hodnotami ako:

```python
MAX_LEVEL = 5
SIRKA_HP_BARU = 20
MIN_POSKODENIE = 1
```

a použi ich všade namiesto čísel roztrúsených v kóde.

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| `ModuleNotFoundError: No module named 'hra'` | spúšťaš z nesprávneho priečinka — musíš byť v koreni projektu |
| `ImportError: cannot import name ...` | kruhový import alebo preklep v mene |
| hra sa spustí dvakrát | chýba `if __name__ == "__main__"` |

## Kontrola

- Prečo `python3 -m hra` a nie `python3 hra/main.py`?
- Načo je `__init__.py`?
- Ako poznáš kruhový import?

➡️ Ďalej: `06_json_a_data.md`
