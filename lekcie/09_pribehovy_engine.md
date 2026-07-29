# Lekcia 09 — Príbehový engine

**Cieľ:** vetvený príbeh úplne v dátach. Engine nepozná ani jednu scénu.

## Python koncepty
Vnorené štruktúry, `.get()` s predvolenou hodnotou, validácia dát,
tabuľka funkcií (dispatch dictionary).

## Formát scény (`hra/data/pribeh_warrior.json`)

```json
{
  "uvod": {
    "text": "Vyhňa tvojho otca vychladla. Z lesa sa ozýva vytie.",
    "volby": [
      {"text": "Vezmi kladivo a choď k lesu", "vedie_na": "les"},
      {"text": "Zostaň v dielni", "vedie_na": "dielna", "efekty": {"xp": 2}}
    ]
  },
  "les": {
    "text": "Spomedzi stromov sa vynorí vlk.",
    "suboj": "vlk",
    "po_suboji": "cesta_hostinec"
  },
  "cesta_hostinec": {
    "text": "Cesta stúpa k hostincu U troch kladív.",
    "volby": [
      {"text": "Pokračuj", "vedie_na": "zbojnici", "podmienka": {"min_level": 2}},
      {"text": "Odpočiň si", "vedie_na": "cesta_hostinec", "efekty": {"hp": 5}}
    ]
  }
}
```

## Systém efektov — dispatch namiesto `if`

```python
def efekt_hp(hra, hodnota):    hra.postava.uzdrav(hodnota)
def efekt_xp(hra, hodnota):    hra.postava.pridaj_xp(hodnota)
def efekt_item(hra, hodnota):  hra.postava.inventar.append(hodnota)

EFEKTY = {"hp": efekt_hp, "xp": efekt_xp, "item": efekt_item}

def aplikuj_efekty(hra, efekty):
    for kluc, hodnota in (efekty or {}).items():
        funkcia = EFEKTY.get(kluc)
        if funkcia is None:
            raise ValueError(f"Neznámy efekt: {kluc}")
        funkcia(hra, hodnota)
```

Nový druh efektu (napr. `rage`) = jedna funkcia + jeden riadok v slovníku.

## Úloha

1. `hra/pribeh.py`: `zobraz_scenu(hra)`, `aplikuj_efekty(hra, efekty)`,
   `splnena_podmienka(postava, podmienka)`.
2. Podmienky: `min_level`, `ma_predmet`, `min_hp`. Nesplnené voľby
   buď skry, alebo zobraz sivo s dôvodom — vyber si a buď dôsledný.
3. Napíš celý Úvod + Kapitolu 1 podľa tvojho zadania:
   kováčov syn → tiene pri lese → prvý boj s vlkom → cesta k hostincu
   (2 boje) → mini-boss **Grimjaw** s otcovým ukradnutým mečom.
4. Grimjawova porážka nech dá cez `efekty` predmet `otcov_mec`.
5. Napíš `over_pribeh(data)`, ktorá skontroluje, že každé `vedie_na`
   ukazuje na existujúcu scénu. Spusti ju pri štarte — chyby v obsahu
   chceš nájsť pri spustení, nie po hodine hrania.

## Kontrola
- Prečo je slovník `EFEKTY` lepší než `if kluc == "hp": ...`?
- Ako pridáš efekt „stratíš predmet" bez zásahu do `aplikuj_efekty`?

➡️ Ďalej: `10_suboj.md`
