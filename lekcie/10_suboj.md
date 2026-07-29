# Lekcia 10 — Ťahový súbojový systém

**Cieľ:** kolá, akcie, log, obrana, koniec boja.

## Python koncepty
Trieda držiaca stav, zoznam ako log, oddelenie „čo sa stalo" od „ako to vypíšem".

## Návrh

```python
class Suboj:
    def __init__(self, postava, nepriatel):
        self.postava = postava
        self.nepriatel = nepriatel
        self.kolo = 1
        self.log = []              # zoznam textov, NIE print
        self.brani_sa = False      # obrana platí len na 1 kolo

    def zapis(self, text):
        self.log.append(text)

    def tah_hraca(self, akcia):    ...
    def tah_nepriatela(self):      ...
    def skoncil(self):
        return not self.postava.zije() or not self.nepriatel.zije()
```

**Kritické pravidlo:** `Suboj` neobsahuje ani jeden `print` a ani jeden
`input`. Vracia stav a log; UI ho vykreslí. Vďaka tomu neskôr rovnaký súboj
poháňa aj grafickú verziu — a dá sa testovať.

## Akcie hráča
`utok`, `obrana`, `kuzlo`, `predmet`, `utek`.

Poradie kola: hráč → kontrola konca → nepriateľ → kontrola konca →
vyprší obrana → `kolo += 1`.

## Obrana
Zvyšuje `celkova_obrana()` o daný bonus do konca nepriateľovho ťahu a napr.
generuje +2 Rage. Nezabudni ju na konci kola vypnúť — inak máš nesmrteľného
hrdinu.

## Poškodenie

```python
def vypocitaj_poskodenie(utok, obrana):
    return max(MIN_POSKODENIE, utok - obrana)
```

Kocku pripočítaš v lekcii 11 — teraz počítaj len so základom.

## Úloha
1. `hra/suboj.py` s triedou `Suboj`.
2. `obrazovka_suboj(hra)` v `obrazovky.py`: vykreslí HP bary oboch strán,
   posledných ~5 riadkov logu, ponuku akcií.
3. Po víťazstve: XP, prípadný loot, prechod na `po_suboji` scénu.
4. Po prehre: obrazovka „Padol si" → menu.
5. Útek: 50 % šanca (`random.random() < 0.5`), pri neúspechu stratíš ťah.

## Kontrola
- Prečo v `Suboj` nesmie byť `print`?
- Kedy presne sa vypína obrana?
- Čo sa stane, ak zabudneš skontrolovať smrť medzi ťahmi?

➡️ Ďalej: `11_kocky_a_nahoda.md`
