# Lekcia 00b — VS Code v dennej práci

**Cieľ:** vedieť sa vo VS Code pohybovať tak, aby ťa nebrzdil.

Krátka lekcia, ale vráť sa k nej, keď ti niečo pôjde pomaly.

---

## Rutina každého sedenia

```
1. Otvor VS Code → File → Open Recent → Game
2. Ctrl + ö          (terminál; (.venv) sa objaví samo)
3. git pull          (ak pracuješ na viacerých počítačoch)
4. Otvor lekciu, píš kód
5. python -m hra     (skús, či to beží)
6. git add . && git commit -m "..."
7. git push
```

## Skratky, ktoré si zapamätaj

| Skratka | Čo robí |
|---------|---------|
| `Ctrl + ö` | terminál sem/preč |
| `Ctrl + Shift + E` | prieskumník súborov |
| `Ctrl + Shift + G` | git panel |
| `Ctrl + P` | rýchle otvorenie súboru podľa mena |
| `Ctrl + Shift + P` | príkazová paleta (**všetko** sa dá cez ňu) |
| `Ctrl + /` | zakomentuj / odkomentuj riadok |
| `Alt + ↑ / ↓` | presuň riadok hore/dole |
| `Shift + Alt + ↓` | zduplikuj riadok |
| `F2` | premenuj premennú **všade naraz** |
| `F12` | skoč na definíciu funkcie |
| `Alt + ←` | späť tam, odkiaľ si skočil |
| `Ctrl + F` | hľadaj v súbore |
| `Ctrl + Shift + F` | hľadaj v celom projekte |
| `Ctrl + ,` | nastavenia |

Dve z nich sú v tomto projekte zlaté: **`F2`** (keď premenuješ `hp` na
`zdravie`, urobí to správne všade) a **`F12`** (keď v `obrazovky.py` uvidíš
`vypocitaj_poskodenie` a chceš vedieť, čo robí).

## Zelené a červené vlnovky

- **Červená vlnovka** = chyba, program nepobeží. Prejdi myšou → uvidíš prečo.
- **Žltá/šedá** = varovanie (nepoužitá premenná, nepoužitý import).
- **Žiarovka 💡** = VS Code vie, ako to opraviť. Klikni a vyber.

Panel `Ctrl + Shift + M` (Problems) ukáže všetky chyby v projekte naraz.

## Debugger — keď `print` nestačí

Toto ťa raz zachráni, tak sa to nauč teraz, kým je kód malý.

1. Klikni **vľavo od čísla riadku** — objaví sa červený bod (breakpoint).
2. `F5` spustí program a **zastaví ho** na tom riadku.
3. Vľavo v paneli *Variables* vidíš **hodnoty všetkých premenných** v tej chvíli.
4. Ovládanie:
   - `F10` — ďalší riadok
   - `F11` — vojdi do funkcie
   - `F5` — pokračuj do ďalšieho breakpointu
   - `Shift + F5` — zastav

Kedy to použiť: „prečo mi vlk uberá 12 HP, keď má útok 4?" → breakpoint
do `vypocitaj_poskodenie`, spusti súboj, pozri sa na skutočné hodnoty.
Za tridsať sekúnd vieš odpoveď, ktorú by si `print`-mi hľadal pol hodiny.

## Rozdelená obrazovka

`Ctrl + \` rozdelí editor na dve časti. Praktické, keď píšeš `suboj.py`
a potrebuješ vidieť `postava.py`.

Ešte lepšie: `Ctrl + K` a potom `V` otvorí náhľad Markdownu — lekciu si
môžeš mať otvorenú vedľa kódu.

## Práca s JSON-om

Od lekcie 06 budeš písať veľa JSON-u. VS Code ti pomôže:
- `Shift + Alt + F` naformátuje súbor (odsadenie, medzery)
- červená vlnovka pri chýbajúcej čiarke ti ušetrí `JSONDecodeError`
- `Ctrl + K` `Ctrl + 0` zbalí všetky bloky, `Ctrl + K` `Ctrl + J` rozbalí

## Nastavenia projektu, ktoré tu už máš

V priečinku `.vscode/` sú tri súbory. Nemusíš ich meniť, ale nech vieš:

| Súbor | Čo robí |
|-------|---------|
| `settings.json` | 4 medzery, formátovanie, nastavenie testov |
| `launch.json` | `F5` spustí celú hru, `input()` funguje |
| `extensions.json` | VS Code ti sám ponúkne správne rozšírenia |

## Čo NErobiť

- ❌ Neuprav súbory v `.venv/` — je to len kópia Pythonu, dá sa kedykoľvek zmazať a vytvoriť znova.
- ❌ Necommituj `.venv/` a `__pycache__/` — sú v `.gitignore` z dobrého dôvodu.
- ❌ Nepoužívaj tabulátory na odsadenie v Pythone.

---

## Úloha

1. Otvor `riesenia/lekcia_03/main.py`.
2. Daj breakpoint na riadok s `return max(MIN_POSKODENIE, utok - obrana)`.
3. Spusti `F5`, zvoľ „1", zadaj meno.
4. Keď sa program zastaví, pozri si v paneli *Variables* hodnoty
   `utok` a `obrana`.
5. Skús `F12` na funkcii `hp_bar` a potom `Alt + ←` na návrat.
6. Vyskúšaj `Ctrl + Shift + F` a nájdi v projekte všetky výskyty slova
   `Grimjaw`.

➡️ Ďalej: `01_prvy_skript.md` — konečne programovanie
