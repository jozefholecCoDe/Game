# Lekcia 17 — Testy

**Cieľ:** meniť kód bez strachu, že si rozbil súboj spred mesiaca.

## Python koncepty
`pytest`, `assert`, fixtures, parametrizácia, testovanie náhody.

## Inštalácia a spustenie

```bash
pip install pytest
pytest -q
```

## Prvý test

```python
# testy/test_suboj.py
from hra.suboj import vypocitaj_poskodenie

def test_obrana_znizuje_poskodenie():
    assert vypocitaj_poskodenie(utok=5, obrana=2) == 3

def test_poskodenie_je_vzdy_aspon_jedna():
    assert vypocitaj_poskodenie(utok=1, obrana=99) == 1
```

Teraz vidíš odmenu za pravidlo „logika nikdy netlačí do konzoly" z lekcie 03.
Funkcia, ktorá len počíta a vracia, sa testuje jedným riadkom. Keby volala
`print` a `input`, otestovať sa nedá.

## Fixture — spoločná príprava

```python
import pytest
from hra.postava import Postava

@pytest.fixture
def kael():
    return Postava("Kael", "warrior", hp_max=30, utok=5, obrana=2)

def test_zranenie_nejde_pod_nulu(kael):
    kael.zran(999)
    assert kael.hp == 0
```

## Testovanie náhody
Preto si v lekcii 11 posielal `rng`:

```python
import random

def test_kocka_je_v_rozsahu():
    rng = random.Random(42)
    for _ in range(1000):
        assert 1 <= hod_kockou(rng, 6) <= 6

def test_seed_je_reprodukovatelny():
    assert hod_kockou(random.Random(1), 20) == hod_kockou(random.Random(1), 20)
```

## Čo testovať (a čo nie)
✅ výpočet poškodenia, prahy levelov, vybavenie predmetov, save→load kolobeh,
   validácia príbehu, tikanie statusov
❌ ako presne vyzerá HP bar, texty scén, farby

## Úloha
1. Vytvor `testy/` a napíš aspoň 12 testov.
2. Povinný test: `uloz()` → `nacitaj()` vráti rovnaký stav postavy.
3. Povinný test: prejdi všetky scény príbehu a over, že každé `vedie_na`
   existuje (to je test tvojho **obsahu**, nie kódu — a chytí preklepy).
4. Spusti `pytest` pred každým commitom.

## Kontrola
- Prečo sa dá testovať `vypocitaj_poskodenie`, ale nie `obrazovka_suboj`?
- Ako otestuješ niečo náhodné?
- Čo je fixture?

➡️ Ďalej: `18_refaktoring.md`
