# Lekcia 23 — Nastavenia a konfigurácia

**Cieľ:** používateľské preferencie, ktoré prežijú reštart hry.

## Python koncepty
Používateľský konfiguračný priečinok, zlúčenie predvolieb s uloženými
hodnotami, prostredie terminálu.

## Kam patrí config
Nie do priečinka s hrou — hráč tam nemá čo zapisovať. Použi domovský adresár:

```python
from pathlib import Path
CONFIG = Path.home() / ".moja_hra" / "nastavenia.json"
```

## Zlúčenie predvolieb — dôležitý vzor

```python
PREDVOLENE = {
    "rychlost_textu": "normalna",   # okamzita / normalna / pomala
    "velkost_textu": "normalna",
    "farby": True,
    "zvuk": True,
    "hlasitost": 70,
    "potvrdenie_ukoncenia": True,
}

def nacitaj_nastavenia() -> dict:
    ulozene = {}
    if CONFIG.exists():
        try:
            ulozene = json.loads(CONFIG.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            ulozene = {}
    return {**PREDVOLENE, **ulozene}     # uložené prepíšu predvolené
```

Tento `{**a, **b}` vzor zaručí, že keď v ďalšej verzii pridáš nové
nastavenie, staré configy nespadnú — chýbajúci kľúč sa doplní z predvolieb.

## Poznámka k „hlasitosti"
Textová hra zvuk nemá. Buď nastavenie priprav do dát a použiješ ho až
s `pygame` (lekcia 24), alebo pridaj jednoduché pípanie cez `\a`.
Nezobrazuj hráčovi nastavenie, ktoré nič nerobí.

## Rýchlosť textu

```python
import time, sys

def vypis_postupne(text, rychlost):
    if rychlost == "okamzita":
        print(text)
        return
    pauza = {"normalna": 0.02, "pomala": 0.05}[rychlost]
    for znak in text:
        sys.stdout.write(znak)
        sys.stdout.flush()
        time.sleep(pauza)
    print()
```

Vždy nechaj hráča preskočiť animáciu klávesou. Nútené pomalé písanie
je najrýchlejšia cesta k tomu, aby hru vypol.

## Úloha
1. `hra/nastavenia.py` + `Stav.NASTAVENIA`.
2. Obrazovka s prepínaním hodnôt (šípky / čísla) a možnosťou „Obnoviť predvolené".
3. Farby cez ANSI kódy, vypnuteľné nastavením `farby`.
4. „Veľkosť textu" v termináli rieš ako šírku layoutu (60 / 80 / 100 znakov).
5. Nastavenia sa uložia hneď po zmene.

## Kontrola
- Prečo config nepatrí do priečinka hry?
- Čo urobí `{**PREDVOLENE, **ulozene}` a prečo v tomto poradí?

➡️ Ďalej: `24_grafika_volitelne.md`
