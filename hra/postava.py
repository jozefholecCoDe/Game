from hra import data_loader

def vytvor_postavu(postava, trieda_id, meno):
    if trieda_id not in data_loader.TRIEDY:
        print("Nesprávny výber triedy!")
        return True

    t = data_loader.TRIEDY[trieda_id]
    if t['odomknute'] == True:
        postava['meno'] = meno
        postava['trieda'] = t['nazov']
        postava['hp'] = t['hp_max']
        postava['hp_max'] = t['hp_max']
        postava['utok'] = t['utok']
        postava['obrana'] = t['obrana']
        postava['zdroj'] = 0
        postava['zdroj_max'] = t['resource']['max']
        postava['level'] = 1
        postava['xp'] = 0
        postava['inventar'] = list(t['startovaci_inventar'])
        return False
    else:
        print("Postava je uzamknuta!")
        return True

def pridaj_do_inventara(postava, predmet):
    postava['inventar'].append(predmet)
