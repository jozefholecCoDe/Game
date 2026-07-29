# Lekcia 00 — Nástroje a Git

**Cieľ:** mať funkčný Python, editor a vedieť uložiť prácu do gitu.

Táto lekcia neobsahuje programovanie hry. Je to príprava dielne. Kováčov syn
si tiež najprv rozkúril vyhňu.

---

## 1. Python

Overenie v termináli:

```bash
python3 --version
```

Chceš `3.10` alebo vyššie. Ak to nefunguje, stiahni z python.org
(pri inštalácii na Windows zaškrtni **Add Python to PATH**).

## 2. Editor

Odporúčam **VS Code** + rozšírenie *Python* od Microsoftu. Zapni si:
- zobrazovanie čísel riadkov,
- automatické ukladanie.

## 3. Terminál — 5 príkazov, ktoré potrebuješ

| Príkaz | Čo robí |
|--------|---------|
| `pwd` | kde som |
| `ls` | čo je tu (Windows: `dir`) |
| `cd nazov` | vojdi do priečinka |
| `cd ..` | o úroveň vyššie |
| `python3 subor.py` | spusti skript |

## 4. Git — tvoja poistka

Git je stroj času pre kód. Bez neho skôr či neskôr niečo pokazíš a nevrátiš.

```bash
git status                      # čo sa zmenilo
git add .                       # priprav zmeny
git commit -m "popis zmeny"     # ulož bod v čase
git log --oneline               # história
git push -u origin <vetva>      # pošli na GitHub
```

**Pravidlo pre správy commitov:** píš, *čo* sa mení, nie *že* sa niečo mení.
- ❌ `zmeny`, `fix`, `asdf`
- ✅ `pridaj uvitaciu obrazovku`, `oprav vypocet obrany v suboji`

---

## Úloha

1. Over `python3 --version`.
2. Vytvor súbor `test.py` s obsahom `print("vyhna hori")`.
3. Spusti ho: `python3 test.py`.
4. Zmaž ho a sprav commit s nejakou drobnou zmenou v `README.md`
   (napr. dopíš svoje meno).

## Kontrola

Vieš odpovedať bez pozerania?
- Ako spustíš Python skript?
- Aký je rozdiel medzi `git add` a `git commit`?
- Čo urobí `cd ..`?

## Slovníček

- **terminál / príkazový riadok** — textové ovládanie počítača
- **repozitár (repo)** — priečinok, ktorý sleduje git
- **commit** — uložený bod v histórii
- **vetva (branch)** — samostatná línia vývoja

➡️ Ďalej: `01_prvy_skript.md`
