# Lekcia 06 — JSON: dáta von z kódu

**Cieľ:** `json`, `pathlib`, kódovanie. Výsledok: triedy postáv a nepriatelia
žijú v súboroch, nie v Pythone. **Toto je srdce tvojej architektúry.**

---

## Prečo

Zatiaľ máš `NEPRIATELIA` napevno v kóde. Problém:

- na pridanie nepriateľa musíš meniť program,
- obsah a logika sú pomiešané,
- Mage a Rogue by znamenali kopírovanie kódu.

Data-driven znamená: **engine je hlúpy, dáta sú múdre.** Engine vie „vezmi
nepriateľa a bojuj". Nevie nič o vlkovi ani o Grimjawovi.

## Teória

### JSON — text, ktorý vyzerá ako Python slovník

```json
{
  "id": "vlk",
  "meno": "Hladný vlk",
  "hp": 12,
  "utok": 4,
  "xp": 10,
  "loot": ["Vlčí tesák"]
}
```

Rozdiely oproti Pythonu, ktoré ťa pobijú:

| Python | JSON |
|--------|------|
| `True` / `False` / `None` | `true` / `false` / `null` |
| `'jednoduché'` úvodzovky | **len** `"dvojité"` |
| čiarka za posledným prvkom je OK | čiarka navyše = chyba |
| komentáre `#` | **žiadne komentáre** |

### Načítanie

```python
import json
from pathlib import Path

DATA = Path(__file__).parent / "data"

def nacitaj(nazov):
    cesta = DATA / f"{nazov}.json"
    with cesta.open(encoding="utf-8") as f:
        return json.load(f)

nepriatelia = nacitaj("nepriatelia")
print(nepriatelia["vlk"]["meno"])
```

Čo tu je dôležité:

- `Path(__file__).parent` — cesta relatívne k **súboru**, nie k tomu, odkiaľ
  hru spustíš. Bez toho ti hra prestane fungovať po `cd` inam.
- `encoding="utf-8"` — bez toho ti diakritika a emoji spravia zlú krv,
  najmä na Windows.
- `with` — súbor sa sám zavrie, aj keď nastane chyba.

### Zápis (budeš potrebovať pri save/load)

```python
with cesta.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

`ensure_ascii=False` zachová `č`, `š`, `⚔️`. `indent=2` spraví súbor
čitateľný pre teba.

---

## Úloha

1. Vytvor priečinok `hra/data/`.
2. Presuň dáta do JSON súborov:

   **`hra/data/triedy.json`** — Warrior aktívny, Mage a Rogue pripravené
   s `"odomknute": false`:
   ```json
   {
     "warrior": {
       "nazov": "Warrior",
       "ikona": "⚔️",
       "odomknute": true,
       "hp_max": 30,
       "utok": 5,
       "obrana": 2,
       "resource": {"id": "rage", "nazov": "Rage", "ikona": "🔥", "max": 10},
       "startovaci_inventar": ["kovacske_kladivo", "d6"]
     },
     "mage": { "...": "vyplň podobne, odomknute: false" },
     "rogue": { "...": "vyplň podobne, odomknute: false" }
   }
   ```
   Mage a Rogue už teraz vyplň poriadne — presne toto máš myslené tým
   „kompletne pripravení v archíve". Engine ich len nezobrazí, kým je
   `odomknute: false`.

   **`hra/data/nepriatelia.json`** — vlk, zbojník, Grimjaw.
   **`hra/data/predmety.json`** — kladivo, vesta, kocky D3–D20.

3. Vytvor `hra/data_loader.py` s funkciou `nacitaj(nazov)` a s načítaním
   všetkého pri štarte:
   ```python
   TRIEDY = nacitaj("triedy")
   NEPRIATELIA = nacitaj("nepriatelia")
   PREDMETY = nacitaj("predmety")
   ```
4. Uprav výber postavy tak, aby zobrazil **len** triedy s `odomknute: true`.
   Nikde v kóde nesmie byť napísané slovo `"warrior"` natvrdo v podmienke.

### Kontrolná otázka k úlohe

Ak by si chcel pridať štvrtú triedu (napr. Ranger), koľko riadkov Pythonu
musíš zmeniť? Správna odpoveď je **nula**. Ak je to viac, tvoj engine ešte
nie je data-driven — nájdi, kde sa pýtaš na konkrétnu triedu.

---

## Časté chyby

| Chyba | Príčina |
|-------|---------|
| `json.decoder.JSONDecodeError: Expecting value` | čiarka navyše, jednoduché úvodzovky, alebo `True` namiesto `true` |
| `FileNotFoundError` | relatívna cesta — použi `Path(__file__).parent` |
| `UnicodeDecodeError` / rozsypaná diakritika | chýba `encoding="utf-8"` |

## Kontrola

- Prečo je cesta cez `Path(__file__).parent` lepšia než `"hra/data/..."`?
- Čo urobí `ensure_ascii=False`?
- Čo je v JSON-e namiesto `None`?

➡️ Ďalej: `07_triedy_a_objekty.md`
