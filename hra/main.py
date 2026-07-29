hp = 30
utok = 5
obrana = 2
rage = 0
kocka = 6
utokCelkom = utok + kocka
trieda = "Warrior"
hraBezi = True
while hraBezi:
    print ("1 - Nová hra /n2 - O hre /n3 - Koniec")
    volba = input ("<")
    if volba == "1":
        print ("==============================")
        print ("         Syn Kováča           ")
        print ("==============================")

        meno = input ("Zadaj meno:")

        print (f"Vitaj {meno}!")
        print (f"Trieda: {trieda}")
        print (f"❤️  HP:        {hp}")
        print (f"⚔️  Útok:      {utokCelkom}")
        print (f"🛡️  Obrana:    {obrana}")
        print (f"🔥 Rage:       {rage}")
        print (f"{2+3}")
        print ("{2+3}")
    elif volba == "2":
        print ("Zatial nič")
    elif volba == "3":
        hraBezi = False

