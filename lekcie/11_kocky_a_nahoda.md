# Lekcia 11 — Kocky a náhoda

**Cieľ:** `random`, seed, čisté funkcie. Kocka je **predmet**, nie schopnosť.

## Python koncepty
Modul `random`, `random.Random` inštancia, návratové hodnoty ako štruktúra,
reprodukovateľnosť pre testy.

## Základy

```python
import random

random.randint(1, 6)          # 1..6 vrátane oboch
random.random()               # 0.0 .. 1.0
random.choice(["a", "b"])
random.choices(["a","b"], weights=[9, 1])   # vážený výber — bude treba v lekcii 19
```

### Seed = reprodukovateľná náhoda

```python
rng = random.Random(42)
rng.randint(1, 6)      # vždy rovnaké pri rovnakom seede
```

Vlož `rng` do `Hra` a používaj **len ten**. Bez toho sa súboj nedá testovať.

## Pravidlo tvojej hry

> Útok bez kocky = len base. S kockou sa hod pripočíta.

```python
def hod_kockou(rng, stien):
    """Vráti hod, alebo 0 ak kocka nie je vybavená."""
    if not stien:
        return 0
    return rng.randint(1, stien)

def hod_vybavenou_kockou(rng, postava):
    kocka = postava.vybavenie.get("kocka")
    stien = kocka.kocka_stien if kocka else 0
    return {"hod": hod_kockou(rng, stien), "stien": stien}
```

Vracaj **slovník / dataclass**, nie holé číslo. V lekcii 19 doňho pribudne
`explozia`, `multiplikator`, `bonus_resource` — a nebudeš musieť prepísať
každé volanie. Toto je práve to miesto, ktoré si označil ako „treba rozšíriť
`rollEquippedDice()`". Navrhni ho tak, aby sa rozšíriť dalo.

## Úloha
1. `hra/kocky.py` s funkciami vyššie.
2. Do `predmety.json` pridaj D3, D4, D6, D8, D10, D12, D20 so `slot: "kocka"`.
3. Napoj hod na `Suboj.tah_hraca` — v logu ukáž rozpis:
   `Útok 5 + D6(4) = 9, obrana 2 → 7 poškodenia`.
4. `Hra` nech má `self.rng = random.Random()`; do celého kódu posielaj `rng`.
   Nikde nevolaj `random.randint` priamo.
5. Sprav prepínač: pri spustení `python3 -m hra --seed 42` sa hra správa
   deterministicky. (Nápoveda: `sys.argv`, alebo modul `argparse`.)

## Kontrola
- Prečo `hod_vybavenou_kockou` vracia slovník a nie číslo?
- Prečo posielaš `rng` namiesto volania `random` priamo?
- Aký je rozdiel medzi `randint(1,6)` a `randrange(1,6)`?

➡️ Ďalej: `12_inventar_a_equipment.md`
