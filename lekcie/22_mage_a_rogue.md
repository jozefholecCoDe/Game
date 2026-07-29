# Lekcia 22 — Návrat Mage a Rogue

**Cieľ:** odomknúť dve triedy z archívu. Toto je záverečná skúška
data-driven dizajnu.

## Ako to má prebehnúť

V `triedy.json` prepneš `"odomknute": false` na `true`. Dopíšeš dáta.
**Python nemeníš.**

Ak to takto nejde, engine niekde vie niečo o Warriorovi. Typické miesta:
- `if postava.trieda_id == "warrior"` kdekoľvek,
- slovo „Rage" napevno v UI namiesto `trieda["resource"]["nazov"]`,
- súbojový log s napísaným „🔥",
- príbeh, ktorý predpokladá kováčovho syna.

Oprav tieto miesta **skôr**, než dopíšeš obsah.

## Čo dopísať

| Trieda | Resource | Charakter | Vlastný príbeh |
|--------|----------|-----------|----------------|
| Mage 🔮 | Mana (regeneruje sa každé kolo) | slabé HP, silné kúzla | `pribeh_mage_k1.json` |
| Rogue 🗡️ | Combo (rastie útokmi, míňa sa naraz) | rýchly, kritické zásahy | `pribeh_rogue_k1.json` |

Ku každej: 3 kúzla (lvl 1/2/3), talenty, štartovací inventár,
preferovaná kocka (Mage → D20 vysoký rozptyl, Rogue → 2×D4).

## Nové mechaniky, ktoré si vyžiadajú engine
Niektoré veci sa dátami spraviť nedajú a to je v poriadku — dôležité je,
aby boli **všeobecné**, nie „warriorské":

- regenerácia resource na začiatku kola → nový kľúč `resource.regen` v dátach
- kritický zásah → vlastnosť kocky/talentu, nie vlastnosť Rogua
- combo, ktoré sa míňa naraz → `resource.spotreba: "vsetko"`

Vždy sa pýtaj: *dá sa to napísať tak, aby to mohla použiť aj štvrtá trieda?*

## Úloha
1. Prejdi celý kód a nájdi každú zmienku o Warriorovi. Odstráň ich.
2. Dopíš dáta pre Mage a Rogue.
3. Prepni `odomknute: true`.
4. Dohraj Kapitolu 1 za všetky tri triedy.
5. Zapíš do `ARCHITEKTURA.md`, čo si musel v engine zovšeobecniť.

## Kontrola
- Koľko riadkov Pythonu si musel zmeniť? Čím menej, tým lepší engine.

➡️ Ďalej: `23_nastavenia.md`
