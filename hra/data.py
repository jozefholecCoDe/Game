NEPRIATELIA = {
    "vlk":     {"meno": "Hladný vlk",  "hp": 12, "utok": 4, "obrana": 0, "xp": 10},
    "zbojnik": {"meno": "Zbojník",     "hp": 18, "utok": 5, "obrana": 1, "xp": 15},
    "grimjaw": {"meno": "Grimjaw",     "hp": 34, "utok": 8, "obrana": 3, "xp": 40},
}

postava = {
    "meno": "",
    "trieda": "",
    "hp": 0,
    "hp_max": 0,
    "utok": 0,
    "obrana": 0,
    "zdroj": 0,
    "level": 0,
    "xp": 0,
    "inventar": [""],
}

def najsilnejsi_nepriatel(nepriatelia):
    najsilnejsi = ""
    najviac_hp = 0
    for kluc, data in nepriatelia.items():
        if data['hp'] > najviac_hp:
            najviac_hp = data['hp']
            najsilnejsi = kluc
    return najviac_hp, najsilnejsi
