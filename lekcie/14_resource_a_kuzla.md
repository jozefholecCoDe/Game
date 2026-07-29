# Lekcia 14 — Resource, kúzla a status efekty

**Cieľ:** Rage 🔥, 3 kúzla na triedu (lvl 1/2/3), status efekty, kniha kúziel.

## Python koncepty
Tabuľka funkcií (opäť), stav s trvaním, filtrovanie zoznamov,
generovanie textu z dát.

## Resource per class
Definícia už je v `triedy.json` (`resource: {id, nazov, ikona, max}`).
Engine nikdy nespomenie slovo „rage" — pracuje s `postava.resource`.

Warrior: +2 pri obrane, +1 pri prijatí zásahu, +3 pri zabití.
Tieto čísla patria do JSON-u, nie do kódu.

## Kúzla (`hra/data/kuzla.json`)

```json
{
  "warrior": [
    {
      "id": "rozdrvenie", "nazov": "Rozdrvenie", "ikona": "💥",
      "level": 1, "cena": 3,
      "popis": "Silný úder za {poskodenie} poškodenia.",
      "ucinky": [{"typ": "poskodenie", "hodnota": 8}]
    },
    {
      "id": "bojovy_rev", "nazov": "Bojový rev", "ikona": "🗣️",
      "level": 2, "cena": 4,
      "ucinky": [{"typ": "status", "cielenie": "nepriatel",
                  "status": "oslabenie", "trvanie": 2, "hodnota": 2}]
    },
    {
      "id": "druhy_dych", "nazov": "Druhý dych", "ikona": "🫁",
      "level": 3, "cena": 6,
      "ucinky": [{"typ": "liecenie", "hodnota": 12}]
    }
  ]
}
```

Kúzlo je odomknuté, keď `postava.level >= kuzlo["level"]`. Nikde nedrž zoznam
„odomknutých" kúziel — počítaj ho:

```python
def dostupne_kuzla(postava, kuzla_data):
    return [k for k in kuzla_data[postava.trieda_id] if postava.level >= k["level"]]
```

## Účinky — dispatch, presne ako efekty v lekcii 09

```python
UCINKY = {
    "poskodenie": ucinok_poskodenie,
    "liecenie":   ucinok_liecenie,
    "status":     ucinok_status,
}
```

## Status efekty

```python
@dataclass
class Status:
    id: str
    trvanie: int          # počet kôl
    hodnota: int
```

Každá bojujúca strana má `self.statusy = []`. Na konci kola:
aplikuj (napr. jed uberie HP), zníž `trvanie`, vyhoď tie s `trvanie <= 0`.

Pri odstraňovaní **nikdy nemaž zo zoznamu počas iterácie** — vytvor nový:
```python
self.statusy = [s for s in self.statusy if s.trvanie > 0]
```

## Kniha kúziel
Obrazovka, ktorá vygeneruje popis **z dát** — vrátane ceny, levelu a účinkov.
Popis s `{poskodenie}` doplň cez `.format(...)`. Zamknuté kúzla zobraz
so zámkom a informáciou „odomkne sa na leveli 2".

## Úloha
1. `hra/kuzla.py`, `hra/statusy.py`.
2. Akcia „Kúzlo" v súboji: zoznam dostupných, kontrola resource, zoslanie.
3. `Stav.KNIHA_KUZIEL` + obrazovka.
4. Statusy tikajú na konci kola a zobrazujú sa pri HP baroch.
5. Nepriatelia môžu mať kúzla tiež — Grimjaw nech má aspoň jedno.

## Kontrola
- Prečo sa dostupnosť kúzla počíta, a nedrží v zozname?
- Prečo nemôžeš mazať zo zoznamu počas `for` cyklu?
- Kde je definované, že Warrior má Rage?

➡️ Ďalej: `15_save_load.md`
