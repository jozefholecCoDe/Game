# Lekcia 21 — Talent tree

**Cieľ:** strom talentov so závislosťami.

## Python koncepty
Graf ako slovník, rekurzívne overenie závislostí, detekcia cyklov,
kreslenie stromu v texte.

## Dáta (`hra/data/talenty.json`)

```json
{
  "warrior": {
    "zelezna_koza":  {"nazov": "Železná koža", "popis": "+2 obrana",
                      "vyzaduje": [], "cena": 1, "efekt": {"obrana": 2}},
    "berserk":       {"nazov": "Berserk", "popis": "+3 útok pod 30 % HP",
                      "vyzaduje": ["zelezna_koza"], "cena": 1,
                      "efekt": {"podmieneny_utok": {"pod_hp_percent": 30, "utok": 3}}},
    "krvavy_ziar":   {"nazov": "Krvavý žiar", "popis": "Rage sa nemíňa pri obrane",
                      "vyzaduje": ["berserk"], "cena": 2, "efekt": {"rage_zamok": true}}
  }
}
```

`vyzaduje` je zoznam — talent môže mať viac rodičov. Preto je to **graf**,
nie strom, a preto potrebuješ kontrolu cyklov.

## Kľúčové funkcie

```python
def moze_odomknut(postava, talent_id, talenty) -> bool:
    talent = talenty[talent_id]
    if talent_id in postava.talenty:
        return False
    if postava.talent_body < talent["cena"]:
        return False
    return all(r in postava.talenty for r in talent["vyzaduje"])

def over_bez_cyklov(talenty) -> None:
    """Vyhodí ChybneData, ak A vyžaduje B a B vyžaduje A."""
```

## Vykreslenie v texte

```
⚔️ WARRIOR — talenty (body: 2)

  ✅ Železná koža      +2 obrana
   └─ ✅ Berserk        +3 útok pod 30 % HP
       └─ 🔒 Krvavý žiar (2 body)  Rage sa nemíňa pri obrane
```

## Úloha
1. `hra/talenty.py` + `Stav.TALENTY`.
2. Talent body: 1 za level (nezávisle od bodu z lekcie 13).
3. Efekty talentov napoj do `celkovy_utok()` / `celkova_obrana()`.
4. `over_bez_cyklov` spusti pri štarte.
5. Talenty ulož do save-u (a doplň test save→load).
6. Aspoň 8 talentov pre Warriora.

## Kontrola
- Prečo je to graf a nie strom?
- Ako zistíš cyklus v závislostiach?

➡️ Ďalej: `22_mage_a_rogue.md`
