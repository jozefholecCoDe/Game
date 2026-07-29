# Lekcia 00 — Založenie projektu od nuly

**Cieľ:** mať Python, VS Code, git a rozbehnutý projekt. Na konci lekcie
spustíš prvý program a uložíš ho do gitu.

Táto lekcia neobsahuje programovanie hry. Je to príprava dielne. Kováčov syn
si tiež najprv rozkúril vyhňu. Vezmi si na ňu pokojne celé jedno sedenie.

> Návod je písaný pre **Windows**. Kde sa macOS/Linux líši, je to v rámčeku.

---

## CMD alebo VS Code? Odpoveď hneď na začiatku

Nie je to buď–alebo. **VS Code má terminál v sebe** (`Ctrl + ö`, alebo
*Terminal → New Terminal*). Sú to tie isté príkazy ako v CMD, len ich píšeš
v okne pod kódom a nemusíš nikam prepínať.

Čiže: píšeš kód vo VS Code, spúšťaš ho v termináli vo VS Code, git ovládaš
tiež z VS Code. Samostatné CMD okno otvárať nebudeš.

Jeden háčik hneď na úvod: **predvolený terminál vo VS Code na Windows nie je
CMD, ale PowerShell.** Väčšina príkazov je rovnaká, jeden rozdiel ťa čaká
nižšie pri virtuálnom prostredí. Nezľakni sa ho, je vyriešený.

---

## 1. Python

### Inštalácia (Windows)

1. Choď na **python.org → Downloads** a stiahni najnovšiu verziu (3.12+).
2. Spusti inštalátor a **ZAŠKRTNI „Add python.exe to PATH"** — je to malé
   políčko celkom dole. Bez neho ti nebude fungovať príkaz `python`
   a budeš to hľadať hodinu.
3. Klikni *Install Now*.

> **macOS:** `brew install python` alebo inštalátor z python.org.
> **Linux:** Python už zvyčajne máš; doinštaluj `sudo apt install python3 python3-venv`.

### Overenie

Otvor CMD (klávesa Windows → napíš `cmd` → Enter) a napíš:

```
python --version
```

Očakávaš niečo ako `Python 3.12.4`.

**Ak to nefunguje:**
- Skús `py --version` (Windows má aj tento príkaz).
- Ak ani to nie, PATH nie je nastavené → odinštaluj Python a nainštaluj znova
  so zaškrtnutým políčkom.
- Ak sa otvorí Microsoft Store, máš zapnuté „app execution aliases" —
  *Nastavenia → Aplikácie → Aliasy na spúšťanie aplikácií* → vypni
  `python.exe` a `python3.exe`.

> **Pozor na názvy:** na Windows je to `python`, na macOS/Linuxe `python3`.
> V lekciách píšem `python3`; na Windows píš `python`. Je to to isté.

---

## 2. VS Code

1. Stiahni z **code.visualstudio.com**, nainštaluj (predvolené voľby stačia,
   ale zaškrtni „Add to PATH" a „Open with Code" v kontextovom menu).
2. Spusti VS Code.
3. Otvor panel rozšírení: `Ctrl + Shift + X`.
4. Nainštaluj:
   - **Python** (od Microsoftu) — bez tohto to nemá zmysel
   - **Pylance** — napovedanie a kontrola (často príde s Pythonom automaticky)
   - **Even Better TOML** a **indent-rainbow** sú príjemné, ale nepovinné

### Nastavenia, ktoré si hneď zapni

`Ctrl + ,` otvorí nastavenia. Do vyhľadávania napíš a zapni:

| Nastavenie | Prečo |
|------------|-------|
| `Files: Auto Save` → `afterDelay` | nebudeš zabúdať ukladať |
| `Editor: Render Whitespace` → `boundary` | uvidíš medzery vs. tabulátory |
| `Editor: Insert Spaces` → zapnuté | Python chce medzery, nie taby |
| `Editor: Tab Size` → `4` | štandard v Pythone |

---

## 3. Projekt — dve cesty

### Cesta A: stiahni si tento projekt (odporúčam)

Lekcie už na GitHube máš. Stačí si ich stiahnuť k sebe.

1. Vo VS Code: `Ctrl + Shift + P` → napíš `Git: Clone` → Enter.
2. Vlož adresu svojho repozitára (`https://github.com/<ty>/Game.git`).
3. Vyber priečinok, kam sa má uložiť (napr. `C:\Users\<ty>\Projekty`).
4. VS Code sa spýta „Would you like to open the cloned repository?" → **Open**.
5. Prepni sa na vetvu s lekciami: dole vľavo v modrom pásiku je názov vetvy —
   klikni naň a vyber `claude/game-learning-project-bcbsar`.

### Cesta B: úplne od nuly

Ak chceš zažiť aj zakladanie projektu:

1. *File → Open Folder* → vytvor nový priečinok `Game` → *Select Folder*.
2. `Ctrl + ö` otvorí terminál (už si v priečinku projektu).
3. V termináli:
   ```
   git init
   ```
4. V bočnom paneli (`Ctrl + Shift + E`) klikni na ikonu „nový súbor"
   a vytvor `README.md`.

Ale aj tak si potom lekcie stiahni — inak nemáš podľa čoho ísť.

### ⚠️ Ak v paletke `Git: Clone` vôbec nie je

Znamená to, že **VS Code nenašiel git** a schoval všetky git príkazy.
Over si v termináli:

```
git --version
```

- `'git' is not recognized` → git nemáš nainštalovaný. Preskoč na sekciu 7
  (Git → Inštalácia), nainštaluj ho, **zavri VS Code úplne** a otvor znova.
  Nie „Reload Window" — VS Code hľadá git len pri štarte.
- Verzia sa vypíše, ale príkaz stále chýba → `Ctrl + ,` → `git.enabled`
  musí byť zaškrtnuté; prípadne nastav `git.path` na
  `C:\Program Files\Git\bin\git.exe`.

Klonovať sa dá aj bez paletky, priamo v termináli — funguje to vždy:

```
cd C:\Users\<tvoje-meno>\Documents
git clone https://github.com/<ty>/Game.git
cd Game
git checkout claude/game-learning-project-bcbsar
code .
```

---

## 4. Virtuálne prostredie (venv)

### Čo to je a prečo

Virtuálne prostredie je **samostatná kópia Pythonu pre jeden projekt**.
Keď doňho nainštaluješ `pytest`, nainštaluje sa len sem, nie do celého
počítača. Bez toho sa ti po piatich projektoch knižnice pobijú.

Priečinok `.venv` sa **necommituje** — je v `.gitignore`.

### Vytvorenie

V termináli VS Code (musíš byť v priečinku projektu):

```
python -m venv .venv
```

Vytvorí sa priečinok `.venv`. Trvá to pár sekúnd.

### Aktivácia

**PowerShell** (predvolený terminál vo VS Code):
```
.venv\Scripts\Activate.ps1
```

**CMD:**
```
.venv\Scripts\activate.bat
```

> **macOS/Linux:** `source .venv/bin/activate`

Keď je aktívne, na začiatku riadku uvidíš `(.venv)`. Vyzerá to takto:

```
(.venv) PS C:\Users\ty\Projekty\Game>
```

### ⚠️ Ak PowerShell odmietne spustiť skript

Uvidíš `... cannot be loaded because running scripts is disabled on this system`.
To je bezpečnostné nastavenie Windows. Oprav ho raz a navždy:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Potvrď `A` (áno pre všetko) a skús aktiváciu znova.

### VS Code to vie sám

`Ctrl + Shift + P` → `Python: Select Interpreter` → vyber ten s `.venv`.
Od tej chvíle ti VS Code aktivuje prostredie automaticky vždy, keď otvoríš
nový terminál. Toto sprav — ušetrí ti to opakované písanie.

Overenie, že to funguje:
```
python -c "import sys; print(sys.prefix)"
```
Cesta musí obsahovať `.venv`.

---

## 5. Prvý program

1. V bočnom paneli vytvor súbor `test.py`.
2. Napíš doňho:
   ```python
   print("vyhna hori")
   ```
3. Spusti ho **jedným z troch spôsobov**:

| Spôsob | Ako | Kedy použiť |
|--------|-----|-------------|
| Terminál | `python test.py` | **toto používaj** — funguje vždy |
| Tlačidlo ▶ | vpravo hore | rýchle skúšanie |
| `F5` (debug) | ladenie po krokoch | keď hľadáš chybu |

### ⚠️ Dôležité pre tvoju hru

Tvoja hra bude používať `input()` — pýtať sa hráča na voľby. To funguje
v **termináli**, nie v „Debug Console". Ak sa ti program pri `input()` zasekne
a nedá sa doňho písať:

`Ctrl + ,` → hľadaj `Python Debugging: Console` → nastav na **`integratedTerminal`**.

(Ak si klonoval tento projekt, mám to už nastavené v `.vscode/launch.json`.)

---

## 6. Terminál — 6 príkazov, ktoré potrebuješ

| Príkaz | Čo robí |
|--------|---------|
| `pwd` (CMD: `cd`) | kde som |
| `ls` (CMD: `dir`) | čo je tu |
| `cd nazov` | vojdi do priečinka |
| `cd ..` | o úroveň vyššie |
| `python subor.py` | spusti skript |
| `cls` (mac/Linux: `clear`) | vyčisti obrazovku |

Dva triky, ktoré ti ušetria hodiny:
- **Šípka hore** zopakuje predchádzajúci príkaz.
- **Tab** doplní názov súboru (napíš `pyt` + Tab).

---

## 7. Git

### Inštalácia

Stiahni z **git-scm.com**, nainštaluj (predvolené voľby stačia).
Reštartuj VS Code, aby ho našiel.

### Nastav sa (raz za život)

```
git config --global user.name "Tvoje Meno"
git config --global user.email "tvoj@email.sk"
```

Použi rovnaký e-mail ako na GitHube, inak ti commity nebude pripisovať.

### Čo git robí

Git je **stroj času pre kód**. Ukladá si body v histórii, ku ktorým sa vieš
kedykoľvek vrátiť. Bez neho skôr či neskôr niečo pokazíš a nevrátiš.

### Príkazy

```
git status                    # čo sa zmenilo
git add .                     # priprav všetky zmeny
git commit -m "popis zmeny"   # ulož bod v čase
git log --oneline             # história
git push                      # pošli na GitHub
```

### Alebo klikaním vo VS Code (rovnako dobré)

`Ctrl + Shift + G` otvorí Source Control panel:

1. Uvidíš zoznam zmenených súborov.
2. Klikni na súbor → vidíš, čo presne si zmenil (vľavo staré, vpravo nové).
3. `+` pri súbore = `git add`.
4. Napíš správu hore a klikni **✓ Commit**.
5. **Sync Changes** = push.

Používaj, čo ti vyhovuje. Ja odporúčam aspoň na začiatku príkazy —
lepšie pochopíš, čo sa deje.

### Ako písať správy commitov

Píš, **čo** sa mení, nie **že** sa niečo mení:

- ❌ `zmeny`, `fix`, `update`, `asdf`
- ✅ `pridaj uvitaciu obrazovku`
- ✅ `oprav vypocet obrany v suboji`

O tri mesiace budeš v histórii niečo hľadať a poďakuješ si.

---

## Úloha

1. Over `python --version`.
2. Otvor projekt vo VS Code a vytvor `.venv`, aktivuj ho.
3. Vytvor `test.py` s `print("vyhna hori")` a spusti ho **v termináli**.
4. Zmaž `test.py`.
5. Dopíš svoje meno do `POSTUP.md` a odškrtni lekciu 00.
6. Sprav commit:
   ```
   git add .
   git commit -m "dokoncena lekcia 00"
   ```
7. Pozri si `git log --oneline`.

---

## Časté problémy

| Problém | Riešenie |
|---------|----------|
| `'python' is not recognized` | PATH — preinštaluj Python so zaškrtnutým „Add to PATH" |
| otvorí sa Microsoft Store | vypni app execution aliases (viď vyššie) |
| `Activate.ps1 cannot be loaded` | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `(.venv)` sa nezobrazuje | zabudnutá aktivácia, alebo zlý interpreter |
| pri `input()` sa nedá písať | prepni debug console na `integratedTerminal` |
| `git: command not found` | git nie je nainštalovaný, alebo si nereštartoval VS Code |
| terminál je v zlom priečinku | `cd` do projektu, alebo otvor priečinok cez *File → Open Folder* |

---

## Kontrola

Vieš odpovedať bez pozerania?
- Ako otvoríš terminál vo VS Code?
- Načo je virtuálne prostredie?
- Aký je rozdiel medzi `git add` a `git commit`?
- Prečo hru spúšťaš v termináli a nie v debug konzole?

## Slovníček

- **terminál / príkazový riadok / CMD / PowerShell** — textové ovládanie počítača
- **PATH** — zoznam miest, kde systém hľadá programy
- **venv** — samostatné prostredie s knižnicami pre jeden projekt
- **repozitár (repo)** — priečinok, ktorého históriu sleduje git
- **commit** — uložený bod v histórii
- **vetva (branch)** — samostatná línia vývoja
- **push / pull** — poslať na GitHub / stiahnuť z GitHubu

➡️ Ďalej: `00b_vs_code_denna_praca.md` (krátke, oplatí sa)
