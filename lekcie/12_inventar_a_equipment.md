# Lekcia 12 — Inventár a equipment

**Cieľ:** 3 sloty (zbraň / brnenie / kocka), vybavenie mení štatistiky.

## Python koncepty
Slovník ako mapa slotov, `@dataclass`, odvodené hodnoty (properties),
premýšľanie o „zdroji pravdy".

## Dátový model

```python
postava.inventar = [Predmet, Predmet, ...]        # čo vlastníš
postava.vybavenie = {"zbran": None, "brnenie": None, "kocka": None}
```

**Zlaté pravidlo:** vybavený predmet **nemení** `postava.utok`. Základ zostáva
základ; bonus sa počíta až v `celkovy_utok()`:

```python
def celkovy_utok(self):
    zbran = self.vybavenie.get("zbran")
    return self.utok + (zbran.bonus_utok if zbran else 0)
```

Prečo? Lebo keby si pri vybavení pripočítal a pri zložení odpočítal, skôr či
neskôr niekde zabudneš odpočítať a štatistiky sa ti pomaly nafúknu. Toto je
najčastejší zdroj chýb v RPG inventároch. Jeden zdroj pravdy, bonusy odvodené.

## Operácie
`vybav(predmet)` — skontroluj slot, starý predmet vráť do inventára.
`zloz(slot)`, `zahod(predmet)`, `pouzi(predmet)` (lektvary).

## Úloha
1. `hra/predmety.py` s `@dataclass Predmet` a načítaním z `predmety.json`.
2. `hra/inventar.py` s operáciami vyššie.
3. `obrazovka_inventar(hra)`: zoznam s číslami, označenie `[vybavené]`,
   výber čísla → vybaviť / zložiť / zahodiť.
4. Súboj nech používa `celkovy_utok()` a `celkova_obrana()`.
5. Otcov meč od Grimjawa nech je najsilnejšia zbraň v hre.

### Test, ktorý si sprav ručne
Vybav a zlož zbraň desaťkrát za sebou. Ak `celkovy_utok()` nie je na konci
rovnaký ako na začiatku, porušil si zlaté pravidlo.

## Kontrola
- Prečo bonus nepripočítavaš priamo do `postava.utok`?
- Čo sa stane so starou zbraňou pri vybavení novej?

➡️ Ďalej: `13_xp_a_levelovanie.md`
