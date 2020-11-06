import random

deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

def choix_carte(chosen_cards):
     jeu = []
        for i in tirage:
            print(i)
            choix = input('y/n:')
            if choix == 'y':
                jeu.append(i)
        return jeu

def machine():
    tirage1, deck_restant = premier_tirage()
    choix1 = choix_carte(tirage1)
    tirage2 = deuxieme_tirage(choix1, deck_restant)
    return tirage2

def decompose_jeu(tirage):
    dic = {}
    keys = [1,2,3,4,5]
    valeur = []
    couleur = []
    for i,k in zip(tirage, keys):
        dic[k] = i.split('-')
    for key in dic.keys():
        valeur.append(dic[key][0])
        couleur.append(dic[key][1])
    return valeur, couleur

def convert_carte(liste):
    for e,i in zip(liste, range(0,5)):
        try:
            liste[i] = int(e)
        except:
            if e == 'J':
                liste[i] = 11
            elif e == 'Q':
                liste[i] = 12
            elif e == 'K':
                liste[i] = 13
            elif e == 'A':
                liste[i] = 1
            else:
                continue
    return liste

def partie(mise, bankroll):
    main = machine()
    g, resultat = gain(main, mise)
    bankroll = bankroll - mise
    bankroll += g
    return resultat, bankroll

def video_poker():
    bankroll = int(input("Dank: "))
    mise_joueur = int(input("Faites vous jeu: "))
    
    while bankroll = partie(mise_joueur, bankroll)
        resultat, bankroll = partie(mise_joueur, bankroll)
        print(resulat)
        print("Bank: " + str(bankroll))
        if bankroll == 0:
            print("Game Over")
            break
        else:
            mise_joueur = int(input("Faites vos jeu: "))
            if bankroll - mise_joueur < 0:
                print("mise trop elevée")
                mise_joueur = int(input("Faites vos jeu: "))