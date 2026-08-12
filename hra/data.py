postava = {
    "meno": "",
    "trieda": "",
    "hp": 0,
    "hp_max": 0,
    "utok": 0,
    "obrana": 0,
    "zdroj": 0,
    "zdroj_max":0,
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
