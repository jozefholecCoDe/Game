# Lekcia 18 — Refaktoring a typové anotácie

**Cieľ:** upratať engine, kým je malý. Toto je bod, po ktorom hra rastie ľahko.

## Python koncepty
Typové anotácie, `mypy`, `ruff`, konštanty, rozdelenie zodpovedností.

## Typové anotácie

```python
def vypocitaj_poskodenie(utok: int, obrana: int) -> int: ...

def dostupne_kuzla(postava: Postava, data: dict[str, list[dict]]) -> list[dict]: ...

def najdi_predmet(id: str) -> Predmet | None: ...
```

Python ich neuplatňuje pri behu — sú pre teba, pre editor a pre kontrolóra:

```bash
pip install mypy ruff
mypy hra/
ruff check hra/
```

`Predmet | None` v návratovom type je najužitočnejšia anotácia v celej hre:
prinúti ťa myslieť na prípad „predmet neexistuje".

## Kontrolný zoznam refaktoringu

- [ ] Žiadny `print` mimo `ui.py` a `obrazovky.py`
- [ ] Žiadny `input` mimo `obrazovky.py`
- [ ] Žiadne magické čísla — všetko v `konstanty.py` alebo v JSON-e
- [ ] Žiadna funkcia dlhšia než ~30 riadkov
- [ ] Žiadny `if trieda_id == "warrior"` — rozdiely patria do dát
- [ ] Každá verejná funkcia má docstring
- [ ] `pytest` prechádza

## Ako refaktorovať bezpečne
1. Testy musia byť zelené **pred** začiatkom.
2. Rob jednu zmenu naraz.
3. Po každej zmene spusti `pytest`.
4. Commituj po každom zelenom kroku.

Refaktoring znamená „mením štruktúru, nie správanie". Ak sa počas neho zmení,
čo hra robí, nerefaktoruješ — píšeš novú funkcionalitu, a to je iná činnosť.

## Úloha
1. Doplň anotácie do `postava.py`, `suboj.py`, `kocky.py`, `levely.py`.
2. Spusti `mypy hra/` a oprav, čo sa dá rozumne opraviť.
3. Prejdi kontrolný zoznam a naprav každý bod.
4. Napíš `ARCHITEKTURA.md`: čo robí ktorý modul a ktorý smerom kam importuje.

## Kontrola
- Vynúti Python typové anotácie pri behu?
- Prečo `Predmet | None` a nie len `Predmet`?
- Aký je rozdiel medzi refaktoringom a novou funkcionalitou?

➡️ Ďalej: `19_specialne_kocky.md`
