# Lekcia 24 — Grafika (voliteľné)

**Cieľ:** rovnaká hra, iné zobrazenie. Ak si dodržal pravidlo „logika
netlačí do konzoly", je to práca na dni, nie na mesiace.

## Tri cesty

| Cesta | Vhodné na | Náročnosť |
|-------|-----------|-----------|
| **Textual** | pekné TUI v termináli: panely, tlačidlá, myš | nízka |
| **pygame** | skutočná grafika, obrázky, zvuk, animácie | stredná |
| **web** (FastAPI + HTML/JS) | pôvodný nápad, hrateľné v prehliadači | vyššia |

Odporúčam **Textual** ako prvý krok — vyzerá to prekvapivo dobre, používa
rovnaký text a nemusíš kresliť ani jeden pixel.

## Podmienka, bez ktorej to nepôjde
Tvoj engine musí byť použiteľný takto:

```python
suboj = Suboj(postava, nepriatel)
suboj.tah_hraca("utok")          # nič nevypíše, nič sa nepýta
print(suboj.log[-1])             # zobrazenie je vec volajúceho
```

Ak `Suboj` niekde volá `input()`, grafická verzia sa nedá napísať bez
prepísania súboja. Vráť sa k lekcii 10 a oprav to.

## Architektúra s dvoma rozhraniami

```
hra/
├── engine/         # postava, suboj, kuzla, kocky, pribeh — bez print/input
├── ui_text/        # doterajšia konzolová verzia
└── ui_pygame/      # nová grafická verzia
```

Obe UI volajú ten istý engine. Testy testujú engine a nezaujíma ich, ktoré
UI beží.

## pygame — minimum

```python
import pygame

pygame.init()
obrazovka = pygame.display.set_mode((960, 600))
hodiny = pygame.time.Clock()

bezi = True
while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False
    obrazovka.fill((20, 18, 24))
    # tu kresli HP bary, text scény, tlačidlá volieb
    pygame.display.flip()
    hodiny.tick(60)
```

Všimni si: je to tá istá `while` slučka ako v lekcii 02, len namiesto
`input()` číta udalosti a namiesto `print()` kreslí.

## Úloha
1. Rozdeľ projekt na `engine/` a `ui_text/`. Testy musia zostať zelené.
2. Vyber si Textual alebo pygame a sprav **jednu** obrazovku — súboj.
3. Over, že konzolová verzia stále funguje.

## A ďalej
Máš hotovú hru a vieš programovať. Ďalšie kroky podľa chuti:
zvuk a hudba, animácie zásahov, viac kapitol, Steam/itch.io build cez
`pyinstaller`, alebo webová verzia — a tam sa ti zíde to HTML/CSS/JS
z tvojho pôvodného nápadu.

🎉 Koniec učebného plánu.
