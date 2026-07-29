# Lekcia 20 — Kapitola 2: písanie obsahu

**Cieľ:** rozšíriť príbeh po hostinci — bez jediného riadku nového Pythonu.

Toto je skúška tvojej architektúry. Ak musíš kvôli novej kapitole meniť
engine, niečo v ňom nie je data-driven. Nájdi to a oprav — je to cennejšie
než samotná kapitola.

## Python koncepty
Žiadne nové. Namiesto toho: **nástroje pre obsah**.

## Čo napísať
- Hostinec: dialóg s hostinským, odpočinok (obnovenie HP za zlato/čas),
  informácie o Grimjawovi a otcovom meči.
- Rozcestie: aspoň 2 rôzne vetvy, ktoré sa neskôr zbiehajú.
- 3–4 nové boje s rastúcou obtiažnosťou.
- Voliteľné stretnutie odomknuté podmienkou (`min_level`, `ma_predmet`).
- Koniec kapitoly s háčikom na Kapitolu 3.

## Rady na obsah
- Rozdeľ príbeh na súbory: `pribeh_warrior_k1.json`, `..._k2.json`,
  a v loaderi ich spoj do jedného slovníka. Jeden 2000-riadkový JSON
  sa neudržiava.
- Každá scéna nech má aspoň 2 voľby, inak to nie je vetvenie, ale odstavec.
- Voľba nech niečo stojí alebo niečo dá — voľba bez následku je len tlačidlo.

## Nástroje, ktoré si napíš (a ušetríš si hodiny)
1. `nastroje/mapa_pribehu.py` — vypíše graf scén a nájde nedosiahnuteľné
   scény alebo slepé uličky.
2. `nastroje/nova_scena.py` — vygeneruje kostru scény do JSON-u.
3. Rozšír validáciu z lekcie 16 aj na nové kapitoly.

## Úloha
1. Napíš Kapitolu 2 (10–15 scén).
2. Spusti mapu príbehu a over, že sa dá dohrať a niet slepých uličiek.
3. Prejdi hru celú od začiatku a zapíš si, čo je nudné alebo nevyvážené.
4. **Nepridal si žiadny Python?** Výborne. Ak áno, napíš si, prečo — a či
   sa to dalo vyriešiť dátami.

➡️ Ďalej: `21_talent_tree.md`
