# Lekcia 07 — Triedy a objekty

**Cieľ:** `class`, `__init__`, metódy, `@dataclass`. Výsledok: `Postava`
a `Nepriatel` ako objekty namiesto holých slovníkov.

---

## Prečo prejsť zo slovníka na triedu

Slovník je fajn na **dáta zvonku** (JSON). Trieda je lepšia na **živý stav**,
lebo:

- preklep `postava["hpp"]` slovník ticho prijme, `postava.hpp` spadne hneď,
- editor ti napovie, čo objekt vie,
- logika býva pri dátach: `postava.zran(5)` namiesto `zran(postava, 5)`.

Pozor na rovnováhu: **JSON zostáva JSON.** Trieda si dáta z JSON-u načíta,
ale sama sa v kóde nezmení na dvadsať `if`-ov. Data-driven princíp platí ďalej.

## Teória

```python
class Postava:
    def __init__(self, meno, trieda_id, hp_max, utok, obrana):
        self.meno = meno
        self.trieda_id = trieda_id
        self.hp_max = hp_max
        self.hp = hp_max
        self.utok = utok
        self.obrana = obrana
        self.level = 1
        self.xp = 0
        self.inventar = []

    def zije(self):
        return self.hp > 0

    def zran(self, kolko):
        """Uberie HP, nikdy pod nulu. Vráti skutočne ubrané množstvo."""
        skutocne = min(kolko, self.hp)
        self.hp -= skutocne
        return skutocne
```

`self` je „ja sám" — konkrétny objekt. Pri volaní ho nepíšeš:

```python
kael = Postava("Kael", "warrior", 30, 5, 2)
kael.zran(7)
print(kael.hp)        # 23
```

### Vytvorenie z dát — kľúčový vzor

```python
    @classmethod
    def z_triedy(cls, meno, trieda_id, triedy_data):
        d = triedy_data[trieda_id]
        return cls(meno, trieda_id, d["hp_max"], d["utok"], d["obrana"])
```

Takto spojíš JSON a triedu. Engine nepozná Warriora — dostane `trieda_id`.

### `@dataclass` — menej písania

```python
from dataclasses import dataclass, field

@dataclass
class Predmet:
    id: str
    nazov: str
    slot: str | None = None      # "zbran" / "brnenie" / "kocka" / None
    bonus_utok: int = 0
    bonus_obrana: int = 0
    kocka_stien: int = 0
```

Dataclass ti sám dopíše `__init__` a slušný výpis. Používaj ho na jednoduché
dátové objekty, obyčajnú `class` na tie, čo majú veľa správania.

### `__str__` — ako sa objekt vypíše

```python
    def __str__(self):
        return f"{self.meno} ({self.hp}/{self.hp_max} HP)"
```

### Dedičnosť — a prečo ju teraz nepotrebuješ

Mohol by si spraviť `class Warrior(Postava)`. **Nerob to.** Rozdiel medzi
triedami je v dátach (`triedy.json`), nie v kóde. Trieda navyše by ti
data-driven dizajn rozbila.

---

## Úloha

1. Vytvor `hra/postava.py` s triedou `Postava`:
   - atribúty: `meno, trieda_id, hp, hp_max, utok, obrana, level, xp,
     resource, resource_max, inventar, vybavenie`
   - metódy: `zije()`, `zran(kolko)`, `uzdrav(kolko)`, `pridaj_xp(kolko)`,
     `celkovy_utok()`, `celkova_obrana()`
   - `@classmethod z_triedy(...)`
2. `celkovy_utok()` nech ráta základ + bonus z vybavenej zbrane.
   Kocku zatiaľ ignoruj — pridáme ju v lekcii 11.
3. Vytvor `hra/nepriatel.py` s triedou `Nepriatel` a `z_dat(id, data)`.
4. Prerob súboj a UI, aby pracovali s objektmi.
5. `uzdrav()` nikdy nesmie prekročiť `hp_max`, `zran()` nikdy pod 0.
   Over si to ručne: `kael.zran(999)` → `hp == 0`, nie `-969`.

### Bonus

Napíš `Postava.__str__` a skús `print(kael)`.

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| `TypeError: ... takes 3 positional arguments but 4 were given` | zabudnutý `self` v definícii metódy |
| `AttributeError: 'Postava' object has no attribute 'hp'` | preklep, alebo priradenie chýba v `__init__` |
| všetky postavy zdieľajú inventár | zoznam si vytvoril ako atribút triedy namiesto v `__init__` |

## Kontrola

- Čo je `self`?
- Prečo `hp` nastavuješ v `__init__`, a nie na úrovni triedy?
- Kedy `@dataclass` a kedy obyčajná trieda?
- Prečo **nerobíme** `class Warrior(Postava)`?

➡️ Ďalej: `08_state_machine.md`
