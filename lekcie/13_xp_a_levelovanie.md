# Lekcia 13 — XP, levelovanie a alokácia bodu

**Cieľ:** max level 5, level-up obrazovka s výberom ⚔️ / 🛡️ / ❤️.

## Python koncepty
Tabuľky namiesto vetvení, `while` pri viacnásobnom postupe, návrat viacerých
hodnôt.

## Prahy v dátach (`hra/data/levely.json`)

```json
{
  "max_level": 5,
  "prahy": {"2": 20, "3": 50, "4": 100, "5": 170},
  "body_za_level": 1,
  "odmeny": {
    "utok":   {"ikona": "⚔️", "popis": "+1 útok",  "utok": 1},
    "obrana": {"ikona": "🛡️", "popis": "+1 obrana", "obrana": 1},
    "hp":     {"ikona": "❤️", "popis": "+10 HP",   "hp_max": 10}
  }
}
```

Odmeny sú dáta, takže pridať štvrtú možnosť (napr. „+2 Rage max") znamená
riadok v JSON-e, nula riadkov Pythonu.

⚠️ V JSON-e sú kľúče vždy text — `"2"`, nie `2`. Pri načítaní ich preveď:
`{int(k): v for k, v in prahy.items()}`.

## Logika

```python
def pridaj_xp(postava, kolko, levely):
    """Pripočíta XP a vráti počet získaných levelov."""
    postava.xp += kolko
    ziskane = 0
    while postava.level < levely["max_level"]:
        prah = levely["prahy"].get(postava.level + 1)
        if prah is None or postava.xp < prah:
            break
        postava.level += 1
        ziskane += 1
    return ziskane
```

`while`, nie `if` — jeden veľký boj môže dať dva levely naraz. Na max leveli
sa XP môže ďalej zbierať (alebo ju zahoď — rozhodni sa a napíš to do kódu).

## Úloha
1. `hra/levely.py` s načítaním a `pridaj_xp`.
2. `Stav.LEVEL_UP` + obrazovka s výberom odmeny. Pri dvoch leveloch naraz
   sa obrazovka zobrazí dvakrát.
3. Po víťaznom súboji: XP → ak level-up, choď na `LEVEL_UP`, inak späť
   do príbehu. (Tu sa ti zíde `hra.predch_stav`.)
4. Pri `+10 HP` zvýš `hp_max` **aj** `hp` — hráč má cítiť odmenu hneď.
5. XP bar v UI: `xp` / prah ďalšieho levelu, na max leveli text `MAX`.

## Kontrola
- Prečo `while` a nie `if`?
- Prečo sú odmeny v JSON-e a nie v `if`-och?
- Čo sa stane s XP na leveli 5?

➡️ Ďalej: `14_resource_a_kuzla.md`
