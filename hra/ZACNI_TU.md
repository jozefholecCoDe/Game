# Sem píš svoj kód

Tento priečinok je zatiaľ prázdny zámerne. Hra vznikne tu, tvojimi rukami.

## Prvý krok

Otvor `lekcie/00_nastroje_a_git.md` a prejdi ním. Potom `01_prvy_skript.md`,
kde vytvoríš `hra/main.py`.

## Ako to tu bude vyzerať okolo lekcie 08

```
hra/
├── __init__.py
├── __main__.py
├── main.py           # hlavná slučka
├── stavy.py          # Enum obrazoviek
├── obrazovky.py      # jedna funkcia = jedna obrazovka
├── postava.py
├── suboj.py
├── kocky.py
├── inventar.py
├── pribeh.py
├── ui.py             # jediné miesto s print()
├── konstanty.py
└── data/
    ├── triedy.json
    ├── nepriatelia.json
    ├── predmety.json
    ├── kuzla.json
    ├── levely.json
    └── pribeh_warrior_k1.json
```

Tento súbor môžeš pokojne zmazať, keď tu budeš mať vlastný kód.
