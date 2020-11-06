import random

deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

def premier_tirage(deck):
    tirage = random.sample(deck,5)
    for i in tirage:
        deck.remove(i)
    return tirage, deck

pt, px = premier_tirage(deck)

def deuxieme_tirage(jeu, deck):
    nb_carte = len(jeu)
    carte_a_tirer = 5 - nb_carte
    nouvelle_carte = random.sample(deck, carte_a_tirer)
    for i in nouvelle_carte:
        jeu.append(i)
    return jeu

def quinte_flush_royale(tirage):
    valeur_gagnante = ['10','J','Q','K','A']
    valeur, couleur = decompose_jeu(tirage)
    if sorted(valeur_gagnante) == sorted(valeur) and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def quinte_flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def comptage_main(main):
    valeurs = {}
    couleurs = {}
    for x in range(len(main)):
        values = main[x].split("-");
        if(values[0] in valeurs):
            valeurs[values[0]] += 1
        else:
            valeurs[values[0]] = 1
            
        if(values[1] in couleurs):
            couleurs[values[1]] += 1
        else:
            couleurs[values[1]] = 1
            
    return valeurs, couleurs

def compter_paires(compte_main):
    paires = 0
    for x in compte_main:
        if(compte_main[x] == 2):
            if(x == "h" or x == "d" or x == "c" or x == "s"):
                pass
            else:
                paires += 1
    return paires

def compter_brelan(compte_main):
    brelan = 0
    for x in compte_main:
        if(compte_main[x] == 3):
            if(x == "h" or x == "d" or x == "c" or x == "s"):
                pass
            else:
                brelan += 1
    return brelan

def compter_carré(compte_main):
    carré = 0
    for x in compte_main:
        if(compte_main[x] == 4):
            if(x == "h" or x == "d" or x == "c" or x == "s"):
                pass
            else:
                carré += 1
    return carré

def compter_quinte(compte_main):
    quinte = 0
    for x in compte_main:
        if(compte_main[x] == 5):
            if(x == "h" or x == "d" or x == "c" or x == "s"):
                pass
            else:
                quinte += 1
    return quinte

def compte_combinaisons_gagnantes(compte_valeurs, compte_couleurs):
    combinaisons = {'paire': 0,
                    'double_paire': 0,
                    'brelan': 0,
                    'carre': 0,
                    'quinte': 0,
                    'quinte_flush': 0,
                    'quinte_flush_royale': 0}
    combinaison_gagnante = None
    if compter_paires(compte_valeurs):
        combinaisons['paire'] = 1
    if compter_paires(compte_valeurs) == 2:
        combinaisons['double_paire'] = 1
    if compter_brelan(compte_valeurs):
        combinaisons['brelan'] = 1
    if compter_carre(compte_valeurs):
        combinaisons['carre'] = 1
    if compter_quinte(compte_valeurs):
        combinaisons['quinte'] = 1
    if compter_quinte_flush(compte_valeurs, compte_couleurs):
        combinaisons['quinte_flush'] = 1
    if compter_quinte_flush_royale(compte_valeurs, compte_couleurs):
        combinaisons['quinte_flush_royale'] = 1
    for combi in combinaisons:
        if combinaisons[combi] == 1:
            combinaison_gagnante = combi
    return combinaison_gagnante

def afficher_resultat_gains(mise, combinaison_gagnante=''):
    if combinaison_gagnante == "paire":
        print("Vous avez une Paire, vous récupérez votre mise!")
        return mise
    elif combinaison_gagnante == "double_paire":
        print("Vous avez une Double Paire, vous doublez votre mise!")
        return mise * 2
    elif combinaison_gagnante == "brelan":
        print("Vous avez un Brelan, vous triplez votre mise!")
        return mise * 3
    elif combinaison_gagnante == "carre":
        print("Vous avez un Carré, vous remportez 25 fois votre mise!")
        return mise * 25
    elif combinaison_gagnante == "quinte":
        print("Vous avez une Quinte, vous remportez 4 fois votre mise!")
        return mise * 4
    elif combinaison_gagnante == "quinte_flush":
        print("Vous avez une Quinte Flush, vous remportez 50 fois votre mise!")
        return mise * 50
    elif combinaison_gagnante == "quinte_flush_royale":
        print("Vous avez une Quinte Flush Royale, vous remportez 250 fois votre mise!")
        return mise * 250
    else:
        print("Aucune combinaison, vous perdez votre mise!")
        return 0
