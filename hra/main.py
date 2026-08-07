from hra import ui
from hra import data
from hra import suboj
from hra import postava as postavy


def hlavna_slucka():
    hra_bezi = True
    while hra_bezi:
        ui.hlavicka()
        ui.menu()
        volba = input("> ")
        if volba == "1":
            meno = input("Zadaj meno: ")
            ui.vyber_triedu()
            trieda = input("Vyber triedu: ")
            if trieda == "1":
                postavy.vytvor_warriora(data.postava, meno)
            elif trieda == "2":
                postavy.vytvor_rogue(data.postava, meno)
            elif trieda == "3":
                postavy.vytvor_mage(data.postava, meno)
            else:
                print("NEPLATNA VOLBA!!!!!!")

            ui.zobraz_postavu(data.postava)
            bar = ui.hp_bar(data.postava)
            print(f"{bar}")
            poskodenie = suboj.vypocitaj_poskodenie(data.NEPRIATELIA ['vlk']['utok'], data.postava['obrana'])
            print(data.postava['hp'])
            aktualne = suboj.zran(data.postava, poskodenie)
            print(f"Spôsobené poškodenie VLKOM: {aktualne}")
            print(data.postava['hp'])
            print("Ziskal si predmet: Kladivo")
            postavy.pridaj_do_inventara(data.postava, "kladivo")
            print(data.postava['inventar'])
            najsilnejsi = data.najsilnejsi_nepriatel(data.NEPRIATELIA)
            print(f"{najsilnejsi}")
        elif volba == "2":
            print("Zatial nič")
        elif volba == "3":
            print(data.postava['inventar'])
        elif volba == "4":
            hra_bezi = False
        else:
            print("NEPLATNA VOLBA!!!!!!")

if __name__ == "__main__":
    hlavna_slucka()
