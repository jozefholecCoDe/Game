hp = 15
utok = 5
obrana = 2
rage = 0
kocka = 6
utokCelkom = utok + kocka

trieda = "Warrior"

maximum = 30
plne = hp * 20 // maximum          # // je celočíselné delenie

def hlavicka ():
    print ("==============================")
    print ("         Syn Kováča           ")
    print ("==============================")

def menu ():
    print ("1 - Nová hra")
    print ("2 - O hre")
    print ("3 - Koniec")

def hlSluscka ():
    hraBezi = True
    while hraBezi:
        hlavicka ()
        menu ()





while hraBezi:
    print ("1 - Nová hra /n2 - O hre /n3 - Koniec")
    volba = input ("< ")
    if volba == "1":


        meno = input ("Zadaj meno:")

        print (f"Vitaj {meno}!")
        print (f"Trieda: {trieda}")
        print (f"❤️  HP:        {hp}")
        print("[" + "█" * plne + "·" * (20 - plne) + f"] {hp}/{maximum}")
        print (f"⚔️  Útok:      {utokCelkom}")
        print (f"🛡️  Obrana:    {obrana}")
        print (f"🔥 Rage:       {rage}")
        print (f"{2+3}")
        print ("{2+3}")
    elif volba == "2":
        print ("Zatial nič")
    elif volba == "3":
        hraBezi = False

