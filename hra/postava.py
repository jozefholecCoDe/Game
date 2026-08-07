def vytvor_warriora(postava, meno):
    postava['meno'] = meno
    postava['trieda'] = "warrior"
    postava['hp'] = 30
    postava['hp_max'] = 30
    postava['utok'] = 5
    postava['obrana'] = 2
    postava['zdroj'] = 0
    postava['level'] = 1
    postava['xp'] = 0
    postava['inventar'] = "D6"

def vytvor_rogue(postava, meno):
    postava['meno'] = meno
    postava['trieda'] = "rogue"
    postava['hp'] = 25
    postava['hp_max'] = 25
    postava['utok'] = 6
    postava['obrana'] = 1
    postava['zdroj'] = 0
    postava['level'] = 1
    postava['xp'] = 0
    postava['inventar'] = "D3"

def vytvor_mage(postava, meno):
    postava['meno'] = meno
    postava['trieda'] = "mage"
    postava['hp'] = 20
    postava['hp_max'] = 20
    postava['utok'] = 10
    postava['obrana'] = 0
    postava['zdroj'] = 0
    postava['level'] = 1
    postava['xp'] = 0
    postava['inventar'] = ""

def pridaj_do_inventara(postava, predmet):
    postava['inventar'].append(predmet)
