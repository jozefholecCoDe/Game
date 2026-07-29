# Lekcia 15 — Save / Load

**Cieľ:** 3 manuálne sloty + auto-save po boji.

## Python koncepty
Serializácia, verzovanie formátu, `pathlib`, atomický zápis, časové značky.

## Čo ukladať
Len **stav**, nie definície. Predmet ulož ako `"otcov_mec"`, nie ako celý
objekt — popis si vytiahneš z `predmety.json` pri načítaní. Save tak zostane
malý a keď opravíš popis predmetu, prejaví sa aj v starých hrách.

```python
def do_slovnika(hra):
    return {
        "verzia": 1,
        "ulozene": datetime.now().isoformat(timespec="seconds"),
        "postava": {
            "meno": p.meno, "trieda_id": p.trieda_id,
            "hp": p.hp, "hp_max": p.hp_max,
            "utok": p.utok, "obrana": p.obrana,
            "level": p.level, "xp": p.xp, "resource": p.resource,
            "inventar": [i.id for i in p.inventar],
            "vybavenie": {slot: (i.id if i else None)
                          for slot, i in p.vybavenie.items()},
        },
        "scena": hra.aktualna_scena,
    }
```

## Verzia formátu
`"verzia": 1` tam daj **hneď**, aj keď ju zatiaľ nepoužiješ. O tri mesiace
zmeníš štruktúru a budeš rád, že vieš rozoznať starý save od nového.

## Atomický zápis
Ak hra spadne uprostred zápisu, máš rozbitý súbor a hráč príde o postup:

```python
docasny = cesta.with_suffix(".tmp")
with docasny.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
docasny.replace(cesta)      # premenovanie je atomické
```

## Kam ukladať
`ulozenia/slot1.json`, `slot2.json`, `slot3.json`, `autosave.json`.
Priečinok vytvor cez `cesta.parent.mkdir(parents=True, exist_ok=True)`
a pridaj `ulozenia/` do `.gitignore` — cudzie savy do repozitára nepatria.

## Úloha
1. `hra/ulozenie.py`: `uloz(hra, slot)`, `nacitaj(slot)`, `zoznam_slotov()`.
2. Obrazovka Uložiť / Načítať: pri každom slote ukáž meno, level, scénu
   a dátum; prázdny slot ako `— prázdne —`.
3. Auto-save po každom víťaznom boji do `autosave.json`.
4. Prepísanie existujúceho slotu si vypýtaj potvrdenie.
5. Poškodený súbor nesmie zhodiť hru — o tom je nasledujúca lekcia.

## Kontrola
- Prečo ukladáš `id` predmetu a nie celý predmet?
- Načo je `"verzia"`?
- Prečo zapisuješ cez dočasný súbor?

➡️ Ďalej: `16_chyby_a_vynimky.md`
