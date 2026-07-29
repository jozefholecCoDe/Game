# Lekcia 19 — Špeciálne efekty kociek (Časť B)

**Cieľ:** vážené šance, „explózia", multiplikátory, resource bonusy, kombinácie.

Toto je rozšírenie `hod_vybavenou_kockou()` z lekcie 11. Ak si ju vtedy
napísal tak, že vracia slovník, tu nemusíš meniť ani jedno volanie.

## Python koncepty
`random.choices` s váhami, rekurzia vs. slučka, skladanie efektov,
štatistické overenie balansu.

## Vlastnosti kocky v dátach

```json
{
  "id": "d6_ohnivá",
  "nazov": "Ohnivá kocka",
  "slot": "kocka",
  "kocka_stien": 6,
  "vlastnosti": {
    "explozia": {"max_opakovani": 3},
    "vazene": {"1": 0.5, "6": 2.0},
    "multiplikator": {"pri_hode": 6, "krat": 2.0},
    "resource_bonus": {"pri_hode_aspon": 5, "hodnota": 2}
  }
}
```

## Explózia

```python
def hod_s_exploziou(rng, stien, max_opakovani=3):
    hody, celkom = [], 0
    for _ in range(max_opakovani + 1):
        hod = rng.randint(1, stien)
        hody.append(hod)
        celkom += hod
        if hod != stien:
            break
    return celkom, hody
```

Použi slučku, nie rekurziu, a **vždy** maj strop. Kocka bez stropu môže
teoreticky bežať donekonečna a hra zamrzne.

## Vážené šance

```python
def hod_vazeny(rng, stien, vahy):
    hodnoty = list(range(1, stien + 1))
    w = [vahy.get(str(h), 1.0) for h in hodnoty]
    return rng.choices(hodnoty, weights=w, k=1)[0]
```

## Výsledok ako štruktúra

```python
@dataclass
class VysledokHodu:
    zaklad: int = 0            # súčet hodov
    hody: list[int] = field(default_factory=list)
    explodovalo: int = 0
    multiplikator: float = 1.0
    bonus_resource: int = 0

    @property
    def celkom(self) -> int:
        return int(self.zaklad * self.multiplikator)
```

UI z toho vie vyskladať pekný log:
`D6: 6💥 → 6💥 → 3 = 15 ×2.0 = 30 (+2 🔥)`

## Balans — over si ho číslami
Napíš skript, ktorý každou kockou hodí 100 000-krát a vypíše priemer,
minimum a maximum. Ak má „ohnivá D6" priemer 12, kým obyčajná D6 má 3,5,
tvoj mini-boss padne na jeden úder.

## Úloha
1. `hra/kocky.py`: `VysledokHodu` + spracovanie všetkých vlastností.
2. Poradie: vážený hod → explózia → multiplikátor → resource bonus.
   Zapíš toto poradie do docstringu — o mesiac si ho nepamätáš.
3. Aspoň 5 špeciálnych kociek v `predmety.json`.
4. Testy: explózia sa zastaví na strope, vážená kocka je v rozsahu,
   multiplikátor sa aplikuje.
5. Balančný skript `nastroje/balans_kociek.py`.

## Kontrola
- Prečo má explózia strop?
- Prečo vraciaš `VysledokHodu` a nie číslo?
- V akom poradí sa efekty skladajú?

➡️ Ďalej: `20_kapitola_2.md`
