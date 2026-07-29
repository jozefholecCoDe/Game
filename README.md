# Hra (pracovný názov) — RPG v Pythone

Textové ťahové RPG s vetveným príbehom, data-driven dizajnom a postupným
rozširovaním. Zároveň je to učebný projekt — hru staviaš krok po kroku
podľa lekcií v priečinku `lekcie/`.

## Prečo Python

Tvoj cieľ je rozbehnúť to v Pythone a pre **túto** hru je to dobrá voľba:

- Hra je ťahová, textová, dátami riadená — nepotrebuje 60 FPS ani grafický engine.
- Python má JSON, triedy, testy a súborové operácie „v krabici" — presne to,
  čo tvoja architektúra (dáta + engine, save/load, inventár) potrebuje.
- Naučíš sa jazyk, ktorý ti neskôr poslúži aj mimo hier.
- Keď budeš chcieť grafiku, pridáš `pygame` alebo `textual` **nad** hotový
  engine — logika sa neprepisuje. Preto od začiatku oddeľujeme engine od zobrazenia.

## Ako to funguje

1. Otvoríš si `lekcie/NN_nazov.md`.
2. Prečítaš teóriu, napíšeš kód sám.
3. Spustíš, otestuješ, commitneš.
4. Až potom porovnáš s `riesenia/lekcia_NN/`.

Nepreskakuj písanie kódu. Čítanie riešenia nie je učenie sa.

## Rýchly štart (Windows + VS Code)

Podrobne je to v `lekcie/00_nastroje_a_git.md` — toto je len zhrnutie.

```powershell
# 1. Otvor priečinok projektu vo VS Code (File → Open Folder)
# 2. Ctrl + ö otvorí terminál
python -m venv .venv
.venv\Scripts\Activate.ps1        # macOS/Linux: source .venv/bin/activate
python --version
```

Ak PowerShell odmietne skript spustiť:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Potom `Ctrl + Shift + P` → `Python: Select Interpreter` → vyber ten s `.venv`.

Samostatné CMD okno nepotrebuješ — terminál je súčasťou VS Code.

## Štruktúra projektu

```
Game/
├── UCEBNY_PLAN.md   # prehľad všetkých 25 lekcií — začni tu
├── POSTUP.md        # zoznam na odškrtávanie + tvoje poznámky
├── lekcie/          # učebné lekcie (čítaš)
├── riesenia/        # referenčné riešenia lekcií 01–03 (AŽ POTOM)
├── hra/             # tvoj kód — sem píšeš
│   └── data/        # JSON dáta: triedy, scény, predmety, kúzla
├── testy/           # testy (od lekcie 17)
└── .vscode/         # nastavenia VS Code (odsadenie, F5, rozšírenia)
```

## Spustenie

```bash
python3 -m hra          # tvoja hra (od lekcie 05)

python3 riesenia/lekcia_01/main.py    # referenčné riešenie
```

## Stav

Kód zatiaľ žiadny — začínaš `lekcie/00_nastroje_a_git.md`.

## Čo hra bude vedieť (podľa zadania)

Hlavné menu a výber postavy · vetvený príbeh so scénami a voľbami ·
ťahový súboj s HP barmi a logom · XP a levely do 5 s alokáciou bodu ·
inventár s 3 slotmi · kocky D3–D20 ako predmety · Rage 🔥 a kúzla ·
kniha kúziel · save/load v 3 slotoch + auto-save · talent tree ·
Warrior aktívny, Mage a Rogue pripravení v archíve.
