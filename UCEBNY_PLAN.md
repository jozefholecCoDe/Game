# Učebný plán — od nuly po hotovú hru

Každá lekcia = **jeden kus Pythonu** + **jeden herný systém**. Nikdy sa neučíš
teóriu „do zásoby" — vždy ju hneď použiješ na hre.

Tempo: 1 lekcia = 1–3 sedenia po ~60–90 min. Celok je na niekoľko mesiacov.
To je normálne. Nikto sa nenaučí programovať za víkend.

---

## Fáza 0 — Nástroje a základy jazyka

| # | Lekcia | Python koncept | Výsledok v hre |
|---|--------|----------------|----------------|
| 00 | Založenie projektu | Python, VS Code, venv, terminál, git | projekt pripravený na prácu |
| 00b | VS Code v dennej práci | skratky, debugger, breakpointy | vieš sa v editore pohybovať |
| 01 | Prvý skript | premenné, `print`, `input`, f-string | uvítacia obrazovka |
| 02 | Rozhodovanie a slučky | `if/elif/else`, `while`, `for` | hlavné menu, ktoré sa opakuje |
| 03 | Funkcie | `def`, parametre, `return`, rozsah premenných | menu rozdelené na funkcie |
| 04 | Zoznamy a slovníky | `list`, `dict`, iterácia, `.get()` | postava ako dáta, nie ako 20 premenných |

## Fáza 1 — Data-driven základ

| # | Lekcia | Python koncept | Výsledok v hre |
|---|--------|----------------|----------------|
| 05 | Moduly a štruktúra | `import`, balíky, `__main__`, `if __name__` | `python3 -m hra` funguje |
| 06 | JSON a súbory | `json`, `open`, `pathlib`, kódovanie | classes.json — Warrior/Mage/Rogue mimo kódu |
| 07 | Triedy a objekty | `class`, `__init__`, metódy, `@dataclass` | `Postava` s HP, útokom, obranou |

## Fáza 2 — Herné systémy

| # | Lekcia | Python koncept | Výsledok v hre |
|---|--------|----------------|----------------|
| 08 | State machine | `Enum`, slovník funkcií, hlavná slučka | prepínanie obrazoviek bez špagety |
| 09 | Príbehový engine | vnorené dáta, validácia, efekty | vetvený príbeh zo scén a volieb |
| 10 | Súboj | ťahy, stav súboja, HP bar v texte | ťahový boj s logom a obranou |
| 11 | Kocky a náhoda | `random`, seed, čisté funkcie | D3–D20 ako predmet, hod sa pripočíta |
| 12 | Inventár a equipment | zoznamy objektov, sloty, mutácia stavu | 3 sloty: zbraň / brnenie / kocka |
| 13 | XP a levelovanie | prahové tabuľky, dáta namiesto `if` | max lvl 5 + alokácia bodu ⚔️🛡️❤️ |
| 14 | Resource a kúzla | polymorfia, status efekty, tikanie kôl | Rage 🔥, 3 kúzla, kniha kúziel |

## Fáza 3 — Robustnosť

| # | Lekcia | Python koncept | Výsledok v hre |
|---|--------|----------------|----------------|
| 15 | Save/Load | serializácia, verzovanie formátu, atomický zápis | 3 sloty + auto-save po boji |
| 16 | Chyby a výnimky | `try/except`, vlastné výnimky, validácia | hra nespadne na zlom JSON-e |
| 17 | Testy | `pytest`, fixtures, testovanie náhody | refaktoruješ bez strachu |
| 18 | Refaktoring | typové anotácie, `mypy`, čistý kód | engine, ktorý sa dá rozširovať |

## Fáza 4 — Obsah a rozšírenia

| # | Lekcia | Téma | Výsledok |
|---|--------|------|----------|
| 19 | Špeciálne efekty kociek (Časť B) | vážené šance, „explózia", multiplikátory | rozšírený `hod_kockou()` |
| 20 | Kapitola 1 a 2 | písanie obsahu v dátach | mini-boss Grimjaw, cesta po hostinci |
| 21 | Talent tree | grafy, závislosti uzlov | strom talentov pre Warriora |
| 22 | Mage a Rogue | znovupoužitie enginu | odomknuté ďalšie 2 classy |
| 23 | Nastavenia a config | používateľské preferencie | hlasitosť, veľkosť textu, obtiažnosť |
| 24 | Grafika (voliteľné) | `pygame` alebo `textual` | rovnaká hra, iné zobrazenie |

---

## Pravidlá, ktoré platia celý čas

1. **Engine nikdy nevie o konkrétnom obsahu.** Žiadne `if meno == "Grimjaw"`.
   Grimjaw je riadok v JSON-e. Toto je tvoj data-driven princíp.
2. **Logika nikdy netlačí do konzoly.** Funkcia, ktorá počíta poškodenie,
   nesmie volať `print`. Vracia výsledok, zobrazenie rieši iná vrstva.
   Vďaka tomu neskôr pridáš grafiku bez prepisovania.
3. **Commituj po každej lekcii.** Malé commity, jasné správy.
4. **Keď niečo nevieš, najprv skús 15 minút sám.** Potom sa pýtaj.
