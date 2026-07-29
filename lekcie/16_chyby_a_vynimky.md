# Lekcia 16 — Chyby, výnimky a validácia

**Cieľ:** hra nespadne na zlom vstupe ani na poškodenom JSON-e.

## Python koncepty
`try/except/else/finally`, vlastné výnimky, `raise`, čítanie tracebacku.

## Čítanie tracebacku
Traceback sa číta **odspodu**. Posledný riadok = typ a správa chyby.
Predposledný blok = súbor a riadok, kde to prasklo. Nezľakni sa dĺžky.

## Základ

```python
try:
    data = json.loads(text)
except json.JSONDecodeError as chyba:
    print(f"Poškodený súbor: {chyba}")
```

Chytaj **konkrétne** výnimky. `except Exception:` (a najmä holé `except:`)
schová aj tvoje vlastné preklepy a ty budeš hodiny hľadať, prečo sa nič nedeje.

## Vlastné výnimky

```python
class HernaChyba(Exception):
    """Základ pre všetky chyby tejto hry."""

class ChybneData(HernaChyba):
    """JSON súbor nezodpovedá očakávanej štruktúre."""

class NedostatokResource(HernaChyba):
    """Na kúzlo nie je dosť Rage."""
```

Vlastná výnimka nesie **význam**. `except NedostatokResource` vieš ošetriť
v UI hláškou; `except KeyError` netušíš, odkiaľ prišiel.

## Dva druhy chýb — rozlišuj ich

| Druh | Príklad | Riešenie |
|------|---------|----------|
| **Chyba hráča** | zadal `x` namiesto čísla | slušná hláška, opýtaj sa znova |
| **Chyba dát/kódu** | scéna ukazuje na neexistujúce id | spadni **hlasno** pri štarte |

Druhú nikdy neschovávaj. Chceš ju vidieť ty pri vývoji, nie hráč po hodine hry.

## Bezpečný vstup

```python
def opytaj_sa_na_cislo(vyzva, min_h, max_h):
    while True:
        odpoved = input(vyzva).strip()
        if not odpoved.isdigit():
            print("Zadaj číslo.")
            continue
        cislo = int(odpoved)
        if min_h <= cislo <= max_h:
            return cislo
        print(f"Zadaj číslo od {min_h} do {max_h}.")
```

## Úloha
1. `hra/chyby.py` s hierarchiou výnimiek.
2. `hra/validacia.py`: pri štarte over všetky JSON-y — chýbajúce kľúče,
   neexistujúce `vedie_na`, kocky bez `kocka_stien`, kúzla bez `cena`.
   Vypíš **zoznam všetkých** problémov naraz, nie len prvý.
3. Nahraď každý `input()` funkciou `opytaj_sa_na_cislo` / `opytaj_sa_na_volbu`.
4. Poškodený save → hláška „Uložená hra je poškodená" a návrat do menu.
5. Ctrl+C (`KeyboardInterrupt`) nech ukončí hru slušne, nie tracebackom.

## Kontrola
- Prečo je holé `except:` zlé?
- Ktoré chyby ošetriť ticho a ktoré nechať spadnúť?
- Ako sa číta traceback?

➡️ Ďalej: `17_testy.md`
