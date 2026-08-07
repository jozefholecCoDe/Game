from hra import konstanty

def vypocitaj_poskodenie(utok, obrana):
    return max(konstanty.MIN_POSKODENIE, utok - obrana)

def zran(ciel, kolko):
    ubrane = min(kolko, ciel['hp'])
    ciel['hp'] -= ubrane
    return ubrane

