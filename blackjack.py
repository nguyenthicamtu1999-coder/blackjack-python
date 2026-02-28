#########################
##### IMPORTATIONS ######
#########################
import time
from random import choice
from pprint import pprint
from random import randint, shuffle
import json

#########################
### RESSOURCES ASCII ####
#########################

titreASCII = [
    '                                 _..._                      .---.                _..._                   ',
    '            .---.             .-\'_..._\'\'.                   |   |             .-\'_..._''.                ',
    '  /|        |   |           .\' .\'      \'.\\    .             \'---\'           .\' .\'      \'.\\    .          ',
    '  ||        |   |          / .\'             .\'|             .---.          / .\'             .\'|          ',
    '  ||        |   |         . \'             .\'  |             |   |         . \'             .\'  |          ',
    '  ||  __    |   |    __   | |            <    |             |   |    __   | |            <    |          ',
    '  ||/\'__ \'. |   | .:--.\'. | |             |   | ____        |   | .:--.\'. | |             |   | ____     ',
    '  |:/`  \'. \'|   |/ |   \\ |. \'             |   | \\ .\'        |   |/ |   \\ |. \'             |   | \\ .\'     ',
    '  ||     | ||   |`" __ | | \\ \'.          .|   |/ \'.         |   |`" __ | | \\ \'.          .|   |/  .      ',
    '  ||\\    / \'|   | .\'.\'\'| |  \'. `._____.-\'/|    /\\  \\        |   | .\'.\'\'| |  \'. `._____.-\'/|    /\\  \\     ',
    '  |/\\\'..\' / \'---\'/ /   | |_   `-.______ / |   |  \\  \\    __.\'   \'/ /   | |_   `-.______ / |   |  \\  \\    ',
    '    `\'-\'`        \\ \\._,\\ \'/            `  \'    \\  \\  \\  |      \' \\ \\._,\\ \'/            `  \'    \\  \\  \\    ',
    '                  `--\'  `"               \'------\'  \'---\'|____.\'   `--\'  `"               \'------\'  \'---\' '
    ]

fondTableASCII = [
    '             ____  _            _     _            _                                     _____                            ____              ',
    '            | __ )| | __ _  ___| | __(_) __ _  ___| | __   __ _  __ _  __ _ _ __   ___  |___ /   _ __   ___  _   _ _ __  |___ \\             ',
    '            |  _ \\| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /  / _` |/ _` |/ _` | \'_ \\ / _ \\   |_ \\  | \'_ \\ / _ \\| | | | \'__|   __) |            ',
    '            | |_) | | (_| | (__|   < | | (_| | (__|   <  | (_| | (_| | (_| | | | |  __/  ___) | | |_) | (_) | |_| | |     / __/             ',
    '            |____/|_|\\__,_|\\___|_|\\_\\/ |\\__,_|\\___|_|\\_\\  \\__, |\\__,_|\\__, |_| |_|\\___| |____/  | .__/ \\___/ \\__,_|_|    |_____|            ',
    '┌─────────────────────────_────────|__/───────────────────|___/───────|___/────────────___──────|_|───────────────_────────────────────────┐',
    '|                        /_\\   _______  _ _ _ __ _ _ _  __ ___   _ __  __ _ _  _ ___  |_  )  _ __  ___ _  _ _ _  / |                       |',
    '|                       / _ \\ (_-<_-< || | \'_/ _` | \' \\/ _/ -_) | \'_ \\/ _` | || / -_)  / /  | \'_ \\/ _ \\ || | \'_| | |                       |',
    '|                      /_/ \\_\\/__/__/\\_,_|_| \\__,_|_||_\\__\\___| | .__/\\__,_|\\_, \\___| /___| | .__/\\___/\\_,_|_|   |_|                       |',
    '└───────────────────────────────────────────────────────────────|_|─────────|__/────────────|_|────────────────────────────────────────────┘'
    ]

dictCartesASCII = {
    '0': [f'┌─────┐',
          f'│┌ ♣ ┐│',
          f'│♥ ? ♦│',
          f'│└ ♠ ┘│',
          f'└─────┘'],
    '2': [f'┌2────┐',
          f'│x    │',
          f'│     │',
          f'│    x│',
          f'└────2┘'],
    '3': [f'┌3────┐',
          f'│x    │',
          f'│  x  │',
          f'│    x│',
          f'└────3┘'],
    '4': [f'┌4────┐',
          f'│x   x│',
          f'│     │',
          f'│x   x│',
          f'└────4┘'],
    '5': [f'┌5────┐',
          f'│x   x│',
          f'│  x  │',
          f'│x   x│',
          f'└────5┘'],
    '6': [f'┌6────┐',
          f'│x   x│',
          f'│x   x│',
          f'│x   x│',
          f'└────6┘'],
    '7': [f'┌7────┐',
          f'│x   x│',
          f'│x x x│',
          f'│x   x│',
          f'└────7┘'],
    '8': [f'┌8────┐',
          f'│x x x│',
          f'│x   x│',
          f'│x x x│',
          f'└────8┘'],
    '9': [f'┌9────┐',
          f'│x x x│',
          f'│x x x│',
          f'│x x x│',
          f'└────9┘'],
    '10':[f'┌10───┐',
          f'│x x x│',
          f'│xx xx│',
          f'│x x x│',
          f'└───10┘'],
    'V': [f'┌V────┐',
          f'│x//─┐│',
          f'││   ││',
          f'│└─//x│',
          f'└────V┘'],
    'D': [f'┌D────┐',
          f'│x//─┐│',
          f'││   ││',
          f'│└─//x│',
          f'└────D┘'],
    'R': [f'┌R────┐',
          f'│x//─┐│',
          f'││   ││',
          f'│└─//x│',
          f'└────R┘'],
    'A': [f'┌A────┐',
          f'│x/ \\ │',
          f'│( x )│',
          f'│ \\ /x│',
          f'└────A┘']
    }

cartoucheASCII = [
    '┌─────────────┐',
    '│             │',
    '│─────────────│',
    '│    LIBRE    │',
    '│─────────────│',
    '│             │',
    '└─────────────┘'
    ]

joueurASCII = [
    '┌─────────────┐',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '└─────────────┘'
    ]

joueurSplitASCII = [
    '┌─────────────┐',
    '│    SPLIT    │',
    '│─────────────│',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '└─────────────┘'
    ]

joueurBustASCII = [
    '┌─────────────┐',
    '│             │',
    '│ ___ _   _ __ _____',
    '│| _ ) | | / _|_   _',
    '│| _ \\ |_| \\__ \\| |',
    '│|___/\\___/|___/|_|',
    '│             │',
    '└─────────────┘'
    ]

banqueASCII = [
    '┌─────────────┐',
    '│$$$ BANQUE $$│',
    '│─────────────│',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '│             │',
    '└─────────────┘'
    ]

banqueBustASCII = [
    '      ┌─────────────┐      ',
    '      │$$$ BANQUE $$│      ',
    '      │─────────────│      ',
    '______ _   _ _____ _____ _ '
    '| ___ \\ | | /  ___|_   _| |',
    '| |_/ / | | \\ `--.  | | | |',
    '| ___ \\ | | |`--. \\ | | | |',
    '| |_/ / |_| /\\__/ / | | |_|',
    '\\____/ \\___/\\____/  \\_/ (_)',
    '      └─────────────┘      '
    ]

#########################
#### SOUS-PROGRAMMES ####
#########################

#########################
###### UTILITAIRES ######
#########################

# Boucle de saisie pour un choix Booléen
def DemanderSaisieBool(choixTrue, choixFalse, texte):
    saisie = None
    while saisie is None:
        saisie = input(texte + f' {choixTrue}/{choixFalse} : ')
        if saisie == choixTrue:
            saisie = True
        elif saisie == choixFalse or saisie == '':
            saisie = False
        else:
            saisie = None
    return saisie

# Boucle de saisie pour un choix dans une liste d'entiers ou de chaînes de caractères
def DemanderSaisieChoix(choix, texte):
    saisie = None
    while saisie is None or saisie not in choix:
        try:
            if choix[0].is_integer:
                saisie = int(input(texte + f' {choix} : '))
        except AttributeError:
            saisie = input(texte + f' {choix} : ')
        except ValueError:
            saisie = None
    return saisie

# Boucle de saisie pour entrer un entier dans une plage définie
def DemanderSaisieEntier(intMin, intMax, text):
    saisie = None
    while saisie is None:
        try:
            saisie = int(input(text + f' [{intMin};{intMax}] : '))
            if saisie < intMin or saisie > intMax:
                saisie = None
        except ValueError:
            saisie = None
    return saisie

# Boucle de saisie pour entrer une chaîne de caractères d'une longueur max'
def DemanderSaisieStr(intMin, intMax, text):
    saisie = None
    while saisie is None:
        try:
            saisie = input(text + f' [{intMin};{intMax}] : ')
            if len(saisie) < intMin or len(saisie) > intMax:
                saisie = None
        except ValueError:
            saisie = None
    return saisie

#########################
##### INITIALISATION ####
#########################

def InitialiserTable(nombrePlaces):
    # Initialise le dictionnaire contenant TOUTES les informations du jeu
    # C'est le dictionnaire que l'on sauvegardera pour enregistrer l'état de la partie
    nouvelleTable = {
        'REGLES': {
            'TABLE_MISES' : [50,100,250,500,1000],
            'ABANDONNER': False,
            'ASSURANCE': 'PEEK',  # PEEK / NO_PEEK
            'SPLIT': {
                'TYPE': 'RANGS',  # RANGS / VALUE
                'MAX': 1,
                'DOUBLE': True
            },
            'DAME_COEUR': {
                'ACTIF': False,
                'SPLIT': False,
                'TABLE': 'A'  # A / B
            },
            'HYPER_BLACKJACK': {
                'ACTIF': False,
                'MISES_MAX': 1
            },
            '2_1_CARTE': {
                'ACTIF': False,
            },
            'JACKPOT_PROGRESSIF': {
                'ACTIF': False,
                'VALEUR_MISE': 0,
                'VALEUR_JACKPOT': 0
            }
        },
        'PLACES': [],
        'STOP': False,
        'BANQUE': {
            'SCORE': 0,
            'CARTES': [],
            'BUST': False
        },
        'SABOT': {
            'RANGS_VALEURS' : {
                '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'V': 10,'D': 10,'R': 10,'A': 11
            },
            'SUITES' : {
                'Carreau': '♦',
                'Coeur': '♥',
                'Pique': '♠',
                'Trèfle': '♣'
            },
            'INFOS_CARTES' : [],
            'ARRET' : False,
            'PIOCHE': [],
            'DÉFAUSSE': []
        },
        'PHASE': 0
    }
    for n in range(nombrePlaces):
        nouvelleTable['PLACES'].append(ReinitialiserPlace())
    return nouvelleTable

def InitialiserJoueur():
    nouveauJoueur = {
                    'LIBRE': False,
                    'JOUEUR_NOM': '',
                    'ROBOT': {
                         'CONTROLE': False,
                         'NIVEAU': 'facile',
                         'MEMOIRE': []  # Contenu mémoire
                    },
                    'CARTES': [],
                    'SCORE' : 0,
                    'BUST' : False,
                    'SPLIT' : [],
                    'DOUBLE': False,
                    'CAPITAL': 0,
                    'MISES': {
                         'DEPART': 0
                    },
                    'ASSURANCE': False
                    }
    return nouveauJoueur

def ReinitialiserPlace():
    placeLibre = {'LIBRE': True}
    return placeLibre

#########################
####### AFFICHAGE #######
#########################

def AfficherTable():
    PrintList(AfficherBanque(3, 3))
    PrintList(fondTableASCII)
    PrintList(AfficherCartouches())
    PrintList(AfficherPlaces(CreerAffichagesCartesJoueurs(0,2,2),1, 3))

    nSplit = 0
    for j in dictTable['PLACES']:
        if not j['LIBRE']:
            if len(j['SPLIT']) > nSplit:
                nSplit = len(j)
    if nSplit >= 1:
        for indexS in range(1, nSplit):
            PrintList(AfficherPlaces(CreerAffichagesCartesJoueurs(indexS,1,1),1, 3))

    time.sleep(1)

def PrintList(liste):
    for ligne in liste:
        print(ligne)

def CreerListeCartes(estLaBanque, cartes, jeuBase, vertical, horizontal):
    affichageCartesJoueur = []
    carteLayoutTemplate = jeuBase[cartes[0]][2]

    # L'index est étendu pour contenir toutes les cartes en fonction de leur décalage vertical
    for indexLigne in range(len(carteLayoutTemplate) + abs(vertical) * len(cartes) - 1):
        nouvelleLigneCarte = ''

        # On parcours chaque carte à chaque ligne
        for indexCarte in range(len(cartes)):
            if estLaBanque and indexCarte == 0 and dictTable['PHASE'] < 4:
                carteLayout = dictCartesASCII['0']
            else:
                carteLayout = jeuBase[cartes[indexCarte]][2]

            debutPositionVerticale = indexCarte * abs(vertical)
            finV = debutPositionVerticale + len(carteLayout) - 1
            debutH = indexCarte * abs(horizontal)

            # On vérifie que la carte doit commencer ou continuer d'être affichée sur cette ligne
            if debutPositionVerticale <= indexLigne <= finV:
                ligneCorrespondante = indexLigne - debutPositionVerticale
                nouvelleLigneCarte = InsererLigne(carteLayout[ligneCorrespondante], nouvelleLigneCarte, debutH)

        # On ajoute la ligne crée à la liste de ce joueur
        affichageCartesJoueur.append(nouvelleLigneCarte)

    return affichageCartesJoueur

def CreerAffichagesCartesJoueurs(iSplit, vertical, horizontal):
    affichageCartes = []
    jeuBase = dictTable['SABOT']['INFOS_CARTES']

    # Pour chaque place, si elle est occupée par une joueuse, on génère l'affichages des cartes de ce joueur
    for index in range(len(dictTable['PLACES'])):
        if not dictTable['PLACES'][index]['LIBRE']:
            joueur = dictTable['PLACES'][index]

            if len(joueur['CARTES']) > 0 and iSplit == 0:
                # On ajoute l'affichage des cartes du joueur à notre liste d'affichage
                cartesJoueur = CreerListeCartes(False,joueur['CARTES'],jeuBase, vertical, horizontal)
                affichageCartes.append(cartesJoueur)

            elif len(joueur['SPLIT']) > 0:
                # On ajoute l'affichage des cartes du premier Split à notre liste d'affichage
                if iSplit < len(joueur['SPLIT']):
                    cartesJoueur = CreerListeCartes(False, joueur['SPLIT'][iSplit]['CARTES'], jeuBase, vertical, horizontal)
                    affichageCartes.append(cartesJoueur)
            else:
                affichageCartes.append([])
        else:
            affichageCartes.append([])

    return affichageCartes

def CreerAffichagesCartesBanque(vertical, horizontal):
    affichageCartesBanque = []
    jeuBase = dictTable['SABOT']['INFOS_CARTES']

    if len(dictTable['BANQUE']['CARTES']) > 0:

        affichageCartesBanque = CreerListeCartes(True, dictTable['BANQUE']['CARTES'], jeuBase, vertical, horizontal)

    return affichageCartesBanque

def AfficherCartouches():
    affichageCartouche = []
    marge = AjouterEspace(CalculMarge(
        fondTableASCII,
        cartoucheASCII,
        len(dictTable['PLACES'])))

    for ligneIndex in range(len(cartoucheASCII)):
        ligneCartouches = ''
        # On parcourt ensuite chaque place et on y applique le layout
        for indexP in range(len(dictTable['PLACES'])):
            ligneCartouches += cartoucheASCII[ligneIndex] + marge
            positionPlaceHorizontale = (len(cartoucheASCII[0]) + len(marge)) * indexP

            if not dictTable['PLACES'][indexP]['LIBRE']:
                joueur = dictTable['PLACES'][indexP]

                # Affichage niveau du bot
                if ligneIndex == 0:
                    if joueur['ROBOT']['CONTROLE']:
                        statutJoueur = f'─Bot: {joueur['ROBOT']['NIVEAU']}─'
                    else:
                        statutJoueur = f'────Human────'

                    ligneCartouches = InsererLigne(statutJoueur,
                                               ligneCartouches,
                                               positionPlaceHorizontale + 1)
                # Affichage du Nom
                elif ligneIndex == 1:
                    nomCentre = CentrerChaine(joueur['JOUEUR_NOM'], 13)
                    ligneCartouches = InsererLigne(nomCentre,
                                                   ligneCartouches,
                                                   positionPlaceHorizontale + 1)
                # Affichage Mise de Depart
                elif ligneIndex == 3:
                    ligneCartouches = InsererLigne(f' MISE : {joueur['MISES']['DEPART']}$',
                                                   ligneCartouches,
                                                   positionPlaceHorizontale + 1)
                # Affichage Assurance
                elif ligneIndex == 4 and joueur['ASSURANCE']:
                    assurance = CentrerChaine(f'Assuré({joueur['MISES']['DEPART']//2}$)',
                                              13)
                    ligneCartouches = InsererLigne(assurance,
                                               ligneCartouches,
                                               positionPlaceHorizontale + 1)
                # Positionnement du Capital
                elif ligneIndex == 5:
                    capitalCentre = CentrerChaine(str(joueur['CAPITAL'])+'$',13)
                    ligneCartouches = InsererLigne(capitalCentre,
                                                   ligneCartouches,
                                                   positionPlaceHorizontale + 1)

        affichageCartouche.append(ligneCartouches)

    return affichageCartouche

def AfficherBanque(paddingV, paddingH):
    affichageBanque = []
    cartesBanque = CreerAffichagesCartesBanque(1, 2)
    marge = AjouterEspace((len(fondTableASCII[0]) - len(banqueASCII[0]))//2)

    if paddingV > 0:
        for n in range(paddingV):
            cartesBanque.insert(0,'')

        # On cherche si il existe une liste de cartes plus longue que le layout
        nbLignes = len(banqueASCII)
        if len(cartesBanque) > nbLignes:
            nbLignes = len(cartesBanque)
        # On parcourt autant de lignes que la totalité du layout de base de la place
        for ligneIndex in range(nbLignes):
            ligneCartes = ''
            # On parcourt ensuite chaque place et on y applique le layout

            if ligneIndex < len(banqueASCII):
                ligneCartes += marge + banqueASCII[ligneIndex]

            if len(dictTable['BANQUE']['CARTES']) > 0:
                if ligneIndex < len(cartesBanque) and len(cartesBanque) > 0:
                    ligneCartes = InsererLigne(cartesBanque[ligneIndex],ligneCartes,len(marge) + paddingH)

            affichageBanque.append(ligneCartes)

    return affichageBanque

def AfficherPlaces(affichageCartesJoueurs, paddingV, paddingH):
    affichagePlaces = []
    # On génère la liste qui contient les affichages de chaque place sur la table
    if paddingV > 0:
        affichageCartesJoueurs = AppliquerPaddingAffichageCartes(affichageCartesJoueurs, paddingV)

    # On cherche si il existe une liste de cartes plus longue que le layout
    nbLignes = PlusLongueListe(affichageCartesJoueurs, joueurASCII)
    marge = AjouterEspace(CalculMarge(fondTableASCII, joueurASCII, len(dictTable['PLACES'])))
    # On parcourt autant de lignes que la totalité du layout de base de la place
    for indexLigne in range(nbLignes):
        lignePlace = ''
        # On parcourt ensuite chaque place et on y applique le layout
        for indexP in range(len(dictTable['PLACES'])):
            player = dictTable['PLACES'][indexP]
            # Si la place n'est pas libre et que le joueur a des cartes on les affiche au dessus du layout de la place
            if not player['LIBRE']:
                positionPlaceHorizontale = (len(joueurASCII[0]) + len(marge)) * indexP
                if indexLigne < len(joueurASCII):
                    lignePlace += joueurASCII[indexLigne] + marge
                # Le joueur possède des cartes on affiche les cartes PAR DESSUS la place
                if len(player['CARTES']) > 0:
                    if indexLigne < len(affichageCartesJoueurs[indexP]) and len(affichageCartesJoueurs[indexP]) > 0:
                        lignePlace = InsererLigne(affichageCartesJoueurs[indexP][indexLigne],
                                                  lignePlace,
                                                  positionPlaceHorizontale + paddingH)
                elif player['BUST']:
                    if indexLigne < len(joueurBustASCII):
                        lignePlace = InsererLigne(joueurBustASCII[indexLigne],
                                              lignePlace,
                                              positionPlaceHorizontale)
            else:
                lignePlace += AjouterEspace(len(joueurASCII[0])) + marge

        affichagePlaces.append(lignePlace)

    return affichagePlaces

def CalculMarge(largeurTotale, largeurElement, nbJoueurs):
    marge = (len(largeurTotale[0]) - len(largeurElement[0]) * nbJoueurs) // (nbJoueurs - 1)
    return marge

def PlusLongueListe(affichagesCartes, liste):
    plusLongueListe = len(liste)
    for affichage in affichagesCartes:
        if len(affichage) > plusLongueListe:
            plusLongueListe = len(affichage)
    return plusLongueListe

def CentrerChaine(chaine, largeur):
    nouvelleChaine = chaine
    if largeur > len(chaine):
        espacement = largeur - len(chaine)
        if espacement % 2 == 0:
            nouvelleChaine = AjouterEspace(espacement//2) + chaine + AjouterEspace(espacement//2)
        else:
            nouvelleChaine = AjouterEspace(espacement//2) + chaine + AjouterEspace((espacement//2)+1)

    return nouvelleChaine

def AjouterEspace(nombre):
    espace = ''
    for _ in range(nombre):
        espace += ' '
    return espace

def InsererLigne(chaineAInserer, chaineCible, index):
    longueurInsertion = len(chaineAInserer)
    longueurLigneReste = len(chaineCible[index:])

    if len(chaineCible) < index:
        chaineCible = chaineCible[:index] + AjouterEspace(index - len(chaineCible)) + chaineAInserer
    elif longueurInsertion >= longueurLigneReste:
        chaineCible = chaineCible[:index] + chaineAInserer
    else:
        chaineCible = chaineCible[:index] + chaineAInserer + chaineCible[index + len(chaineAInserer):]
    return chaineCible

def AppliquerPaddingAffichageCartes(affichage, vertical):
    nouvelAffichage = affichage.copy()
    for cartes in nouvelAffichage:
        for n in range(vertical):
            cartes.insert(0,'')
    return nouvelAffichage

#########################
######## CARTES #########
#########################

def CreerJeu(sabotA):
    nouveauDeck = {}
    for suite in sabotA['SUITES']:
        for rang in sabotA['RANGS_VALEURS']:
            idCarte = f'{rang}:{suite}'
            nouveauDeck[idCarte] = rang, suite, ConvertirSymboleCarte(dictCartesASCII[rang], sabotA['SUITES'][suite])
    return nouveauDeck

def ConvertirSymboleCarte(layoutCarte, symboleSuite):
    layoutConvertit = layoutCarte.copy()
    for indexListe in range(len(layoutCarte)):
        layoutConvertit[indexListe] = layoutConvertit[indexListe].replace('x', symboleSuite,-1)
    return layoutConvertit

def CreerSabot(jeuBase):
    nouveauSabot = []
    for n in range(6):
        for carte in jeuBase:
            nouveauSabot.append(carte)
    return nouveauSabot

def CouperPaquet(paquet):
    # Simule une coupe de carte : Sépare une liste en deux et met la première partie à la fin de la liste
    positionCoupe = randint(1,len(paquet))
    paquet = paquet[positionCoupe:] + paquet[:positionCoupe]
    return paquet

def MelangerSabot(sabotAMelanger):
    # Routine de mélange officielle des salles de casino
    nbrPile = randint(2, 6)
    sabotPretAJouer = []
    assemblage = []
    # les jeux de cartes sont séparés en plusieurs tas, chacun mélangé et coupé deux fois.
    for n in range(0,nbrPile):
        pile = sabotAMelanger[n * len(sabotAMelanger) // nbrPile:(n + 1) * len(sabotAMelanger) // nbrPile]
        for j in range(2):
            shuffle(pile)
            CouperPaquet(pile)
        assemblage.append(pile)
    shuffle(assemblage)
    # Après cette étape, le jeu est rassemblé, coupé une fois par le croupier et une deuxième fois par un joueur.
    for partie in assemblage:
        sabotPretAJouer += partie
    shuffle(sabotPretAJouer)
    CouperPaquet(sabotPretAJouer)

    return sabotPretAJouer

def PlacerCarteArret(sabotA):
    # Une carte d'arrêt est placée de manière aléatoire sans jamais laisser une partie du sabot inférieure à UN jeu de base.
    carteArret = 'X:CARTE_ARRET'
    positionCarteArret = randint(len(sabotA['INFOS_CARTES']), len(sabotA['PIOCHE']) - len(sabotA['INFOS_CARTES']))
    sabotA['PIOCHE'].insert(positionCarteArret, carteArret)

def VerifierSabot(sabotA):
    # TEST de l'intégrité du paquet de carte après le mélange :
    # Comptage du total des cartes du paquet et comparaison des exemplaires de chaque carte avec le jeu de base
    # Renvoie True si tout correspond et False + liste des cartes manquantes sinon
    verificationCartes = {}
    cartesManquantes = {}
    cartesSupplementaires = {}

    for carte in sabotA['PIOCHE']:
        if carte not in verificationCartes:
            verificationCartes[carte] = 1
        else:
            verificationCartes[carte] += 1
    sorted(verificationCartes)
    sorted(sabotA['INFOS_CARTES'])

    for exemplaireCarte in sabotA['INFOS_CARTES']:
        if exemplaireCarte not in verificationCartes:
            cartesManquantes[exemplaireCarte] = 6
        else:
            nombreExemplaires = verificationCartes[exemplaireCarte]
            if nombreExemplaires < 6:
                cartesManquantes[exemplaireCarte] = 6 - nombreExemplaires
            elif nombreExemplaires > 6:
                cartesSupplementaires[exemplaireCarte] = nombreExemplaires - 6

    if len(cartesManquantes) > 0 or len(cartesSupplementaires) > 0:
        return False, cartesManquantes, cartesSupplementaires
    else :
        return True, cartesManquantes, cartesSupplementaires

def TesterIntegriteSabot(sabotA):
    # Test de l'intégrité du Sabot pour vérifier que toutes les cartes sont bien présente
    resultatTestSabot = VerifierSabot(sabotA)
    if not resultatTestSabot[0]:
        print('!!! ATTENTION !!! Le sabot n\'est pas conforme !!! ATTENTION !!!')
        pprint(resultatTestSabot[0])

def Piocher(sabotA):
    # Vérifie si la carte d'arrêt est atteinte et change la variable de vérification
    if sabotA['PIOCHE'][0] == 'X:CARTE_ARRET':
        sabotA['PIOCHE'][0].remove(0)
        sabotA['ARRET'] = True
    # Prends la première carte de la pioche et la met dans la liste du joueur
    carte = sabotA['PIOCHE'].pop(0)
    return carte

def DefausserCartes(cartes, sabotA):
    for carte in cartes:
        sabotA['DÉFAUSSE'].append(carte)
    cartes.clear()

def ValeurCarte(carte):
    return dictTable['SABOT']['RANGS_VALEURS'][RangCarte(carte)]

def RangCarte(carte):
    return dictTable['SABOT']['INFOS_CARTES'][carte][0]

def SuiteCarte(carte):
    return dictTable['SABOT']['INFOS_CARTES'][carte][1]

def LayoutCarte(carte):
    return dictTable['SABOT']['INFOS_CARTES'][carte][2]

#########################
########## JEU ##########
#########################

def AttribuerPlace(place, index, reglesPartie):
    attribution = place
    if place['LIBRE']:
        choixChangement = DemanderSaisieBool('oui','non',
                                     f'Place n°{index+1} libre, ajouter un nouveau joueur ?')
    else:
        if place['CAPITAL'] < reglesPartie['TABLE_MISES'][0]:
            print(f'Le capital de {place['NOM_JOUEUR']} est insuffisant pour continuer à jouer. Bye, bye {place['NOM_JOUEUR']} :.(')
            choixChangement = True
        else:
            choixChangement = DemanderSaisieBool('partir','rester',
                                                 f'La place n°{index} est occupée par {place['JOUEUR_NOM']} : ')

    if choixChangement:
        choixTypeJoueur = DemanderSaisieChoix(['humain', 'robot', 'libre'],
                                              'Qui va occuper cette place ?')

        if choixTypeJoueur == 'robot' or choixTypeJoueur == 'humain':
            InitialiserJoueur()
            attribution['JOUEUR_NOM'] = DemanderSaisieStr(1, 12,
                                                      'Entrez un nom pour le nouveau joueur : ')
            if choixTypeJoueur == 'robot':
                attribution['ROBOT']['CONTROLE'] = True
                attribution['ROBOT']['NIVEAU'] = DemanderSaisieChoix(['facile', 'normal', 'expert'],
                                                                     'Choisissez le niveau du robot : ')

            attribution['CAPITAL'] = ChoisirCapital(attribution)

        else:
            attribution = ReinitialiserPlace()



    return attribution

def ChoisirCapital(joueur):
    capitalDepart = 1000
    if not joueur['ROBOT']['CONTROLE']:
        capitalDepart = DemanderSaisieEntier(50, 1000,
                                             f'Saisissez le capital de départ de {joueur['JOUEUR_NOM']} : ')
    else:
        if joueur['ROBOT']['NIVEAU'] == 'facile':
            capitalDepart = 1000
        if joueur['ROBOT']['NIVEAU'] == 'normal':
            capitalDepart = 1000
        if joueur['ROBOT']['NIVEAU'] == 'expert':
            capitalDepart = 1000

    return capitalDepart

def ChoisirMise(joueur, reglesPartie):
    choixMise = None
    if not joueur['ROBOT']['CONTROLE']:
        while choixMise is None:
            choixMise = DemanderSaisieChoix(reglesPartie['TABLE_MISES'], 'Choisissez votre mise de départ : ')
            if choixMise > joueur['CAPITAL']:
                choixMise = None

    else:
        multMise = 1
        if joueur['ROBOT']['NIVEAU'] == 'facile':
            multMise = 2
        if joueur['ROBOT']['NIVEAU'] == 'normal':
            multMise = 3
        if joueur['ROBOT']['NIVEAU'] == 'expert':
            multMise = 4
        for mise in reglesPartie['TABLE_MISES']:
            if joueur['CAPITAL'] >= mise * multMise:
                choixMise = mise

    return choixMise

def ProposerAssurance(joueur):
    choix = False
    if joueur['MISES']['DEPART']//2 < joueur['CAPITAL']:
        if not joueur['ROBOT']['CONTROLE']:
            choix = DemanderSaisieBool('oui', 'non',
                                                f'Voulez-vous vous Assurer contre le Blackjack de la Banque ? ')
        else:
            if joueur['ROBOT']['NIVEAU'] == 'facile':
                choix = choice([True,False])
            if joueur['ROBOT']['NIVEAU'] == 'normal':
                if joueur['SCORE'] > 17:
                    choix = True
            if joueur['ROBOT']['NIVEAU'] == 'expert':
                if joueur['SCORE'] == 21:
                    choix = True

    return choix

def ProposerSplit(joueur, cartes):
    choix = False
    # Si le maximum de split n'est pas atteint et que le joueur possède suffisamment de capital, on regarde ses cartes.
    if len(joueur['SPLIT']) < dictTable['REGLES']['SPLIT']['MAX'] and joueur['CAPITAL'] >= joueur['MISES']['DEPART']:
        # Si ses cartes forment une paire, selon les règles de la partie (par valeurs ou par rangs) on propose de split.
        if ((dictTable['REGLES']['SPLIT']['TYPE'] == 'RANGS' and
             (RangCarte(cartes[0]) == RangCarte(cartes[1])))
            or
            (dictTable['REGLES']['SPLIT']['TYPE'] == 'VALEURS' and
             (ValeurCarte(cartes[0]) == ValeurCarte(cartes[1])))):

                if not joueur['ROBOT']['CONTROLE']:
                    choix = DemanderSaisieBool('oui', 'non',
                                                    f'Voulez-vous séparer votre paire ? ')
                else:
                    # par défaut le robot choisi de split
                    '''if joueur['ROBOT']['NIVEAU'] == 'facile':
                    if joueur['ROBOT']['NIVEAU'] == 'normal':
                    if joueur['ROBOT']['NIVEAU'] == 'expert':'''
                    choix = True

    return choix

def NouveauSplit(carte, mise):
    nouveauSplit = {
        'CARTES': [carte],
        'SCORE': 0,
        'BUST': False,
        'MISES': {
            'DEPART':mise
        }
    }
    return nouveauSplit

def Splitter(actif, joueur, nb):
    joueur['CAPITAL'] -= actif['MISES']['DEPART']
    for n in range(nb):
        joueur['SPLIT'].append(NouveauSplit(actif['CARTES'].pop(0), actif['MISES']['DEPART']))

def ProposerDouble(actif, joueur):
    choix = False
    if joueur['CAPITAL'] > joueur['MISES']['DEPART']:
        if not joueur['ROBOT']['CONTROLE']:
            choix = DemanderSaisieBool('oui', 'non',
                                       f'Voulez-vous doubler votre mise et ne prendre qu\'une seule carte ? ')
        else:
            if joueur['ROBOT']['NIVEAU'] == 'facile' and actif['SCORE'] <= 17:
                choix = choice([True,False])

            if joueur['ROBOT']['NIVEAU'] == 'normal':
                if 7 <= actif['SCORE'] <= 11 and joueur['CAPITAL'] > joueur['MISES']['DEPART']*2:
                    choix = choice([True,False])

            if joueur['ROBOT']['NIVEAU'] == 'expert':
                if actif['SCORE'] == 10 and joueur['CAPITAL'] > joueur['MISES']['DEPART']*2:
                    choix = choice([True,False])

                elif 8 <= actif['SCORE'] <= 11 and joueur['CAPITAL'] > joueur['MISES']['DEPART']*4:
                    choix = choice([True,False])

    return choix

def Doubler(actif, joueur):
    actif['DOUBLE'] = True
    joueur['CAPITAL'] -= actif['MISES']['DEPART']
    actif['MISES']['DEPART'] *= 2

def VerifierScore(actif):
    bust = False
    actif['SCORE'] = CalculerScore(actif['CARTES'])
    if actif['SCORE'] > 21:
        actif['BUST'] = True
        bust = True
    return bust

def ProposerCarte(joueur):
    choix = False
    if not joueur['ROBOT']['CONTROLE']:
        choix = DemanderSaisieBool('oui', 'non',
                                        f'Voulez-vous une carte supplémentaire ? ')
    else:
        if joueur['ROBOT']['NIVEAU'] == 'facile' and joueur['SCORE'] < 19:
                choix = True
        if joueur['ROBOT']['NIVEAU'] == 'normal' and joueur['SCORE'] < 18:
                choix = True
        if joueur['ROBOT']['NIVEAU'] == 'expert' and joueur['SCORE'] < 17:
                choix = True
            # TODO : Modifier avec la fonction de Tu

    return choix

def ResultatMise(actif, banqueA):
    resultat = 0
    if actif['SCORE'] > banqueA['SCORE'] or banqueA['BUST']:
        print(f'{joueurActif['JOUEUR_NOM']} a gagné sa mise avec un score de {actif['SCORE']} contre {banqueA['SCORE']} !')
        resultat = actif['MISES']['DEPART'] * 2
        actif['MISES']['DEPART'] = 0
    elif actif['SCORE'] == banqueA['SCORE']:
        print(f'{joueurActif['JOUEUR_NOM']} est a égalité avec un score de {actif['SCORE']} contre {banqueA['SCORE']} !')
        resultat = actif['MISES']['DEPART']
        actif['MISES']['DEPART'] = 0
    else:
        print(f'{joueurActif['JOUEUR_NOM']} a perdu sa mise avec un score de {actif['SCORE']} contre {banqueA['SCORE']} !')
        actif['MISES']['DEPART'] = 0
    return resultat

def CalculerScore(cartes):
    # cartes: liste de tuples (rang, suite), ex : ('A', 'Cœur')
    # Utilise rangsCartes pour les valeurs et gère l'As (11 ou 1)
    total = 0
    nb_as = 0
    for carte in cartes:
        valeur = ValeurCarte(carte)
        total += valeur
        if carte[0] == 'A':
            nb_as += 1
    # si on dépasse 21, on convertit des As de 11 → 1 autant que nécessaire
    while total > 21 and nb_as > 0:
        total -= 10
        nb_as -= 1
    return total

def SauvegarderTable(sauvegarde):
    sauvegarde = f'SAVES/{sauvegarde}.json'
    saveOptions = {'sort_keys': True, 'indent': 4}
    with open(sauvegarde, 'w') as jsonFile:
        json.dump(dictTable, jsonFile, **saveOptions)
    return sauvegarde

def ChargerTable(sauvegarde):
    sauvegarde = f'SAVES/{sauvegarde}.json'
    with open(sauvegarde, 'r') as jsonFile:
        table = json.load(jsonFile)
    return table

#########################
## PROGRAMME PRINCIPAL ##
#########################

PrintList(titreASCII)

dictTable = {}
chargerPartie = False

# Possibilité de charger une partie, auquel cas, on ne change pas les paramètres des places de la table
if DemanderSaisieBool('oui', 'non', 'Charger une partie ?'):
    nomSave = DemanderSaisieStr(1, 12, 'Entrez le nom de la sauvegarde : ')
    dictTable = ChargerTable(nomSave)
    chargerPartie = True
else:
    # Nombre de tables par défaut = 5
    dictTable = InitialiserTable(5)

# On demande si les paramètres par défaut doivent être changés, si oui, on liste les options
if DemanderSaisieBool('oui','non', f'Personnaliser les règles du jeu par défaut ?'):
    # Nombre de places :
    dictTable = InitialiserTable(DemanderSaisieEntier(
        1,7,f'Nombre de places pour cette table : '))
    # Abandon :
    dictTable['REGLES']['ABANDONNER'] = (DemanderSaisieBool(
        'oui', 'non', f'Autoriser l\'abandon ? '))
    # Assurance :
    dictTable['REGLES']['ASSURANCE'] = (DemanderSaisieChoix(
        ['PEEK', 'NO_PEEK'], f'Définissez le type d\'Assurance : '))
    # Split Type:
    dictTable['REGLES']['SPLIT']['TYPE'] = (DemanderSaisieChoix(
        ['VALEURS', 'RANGS'], f'Définissez le critère pour effectuer un Split : '))
    # Split Max:
    dictTable['REGLES']['SPLIT']['MAX'] = (DemanderSaisieEntier(
        1, 10,f'Définissez le nombre maximum de Split consécutifs : '))
    # Split Double:
    dictTable['REGLES']['SPLIT']['DOUBLE'] = (DemanderSaisieBool(
        'oui', 'non', f'Autoriser le Double sur les Split ? '))

    '''# On demande si on veut ajouter des règles optionnelles :
    if DemanderSaisieBool(
            'oui', 'non', f'Ajouter des règles optionnelles ? '):
        # Dame de cœur :
        dictTable['REGLES']['DAME_COEUR']['ACTIF'] = (DemanderSaisieBool(
                'oui', 'non', f'Voulez-vous ajouter l\'option Dame de Coeur ? '))
        # Hyper Blackjack :
        dictTable['REGLES']['HYPER_BLACKJACK']['ACTIF'] = (DemanderSaisieBool(
                'oui', 'non', f'Voulez-vous ajouter l\'option Hyper Blackjack ? '))
        # 2 + 1 Cartes :
        dictTable['REGLES']['2_1_CARTE']['ACTIF'] = (DemanderSaisieBool(
                'oui', 'non', f'Voulez-vous ajouter l\'option 2+1 Carte ? '))
        # Jackpot Progressif :
        dictTable['REGLES']['JACKPOT_PROGRESSIF']['ACTIF'] = (DemanderSaisieBool(
                'oui', 'non', f'Voulez-vous ajouter l\'option Jackpot Progressif ? '))'''

#### PHASE 0 : MISE EN PLACE DE LA TABLE #########################################
if dictTable['PHASE'] == 0:

    jeuBasePourProba = CreerJeu(dictTable['SABOT'])
    # le jeu de base contient le template des jeux utilisés
    dictTable['SABOT']['INFOS_CARTES'] = CreerJeu(dictTable['SABOT'])
    # le sixain est l'assemblage de 6 jeux de base
    dictTable['SABOT']['PIOCHE'] = MelangerSabot(CreerSabot(dictTable['SABOT']['INFOS_CARTES']))
    # Test de l'intégrité du Sabot pour vérifier que toutes les cartes sont bien présente
    TesterIntegriteSabot(dictTable['SABOT'])
    # On place la carte d'arrêt, quand on la pioche, on passe la variable à True et on mélange au prochain tour.
    PlacerCarteArret(dictTable['SABOT'])

    AfficherTable()


    dictTable['PHASE'] = 1

# 0. Attribution des variables de raccourci aux éléments de la bibliothèque principale :
banque = dictTable['BANQUE']
regles = dictTable['REGLES']
sabot = dictTable['SABOT']
places = dictTable['PLACES']

#### BOUCLE DE JEU #####################################################################################################

while not dictTable['STOP']:

    #### PHASE 1 : PREPARATION #########################################
    if dictTable['PHASE'] == 1:

        modifTable = True
        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE']:
                modifTable = False
        if not modifTable :
            modifTable = DemanderSaisieBool('oui', 'non',
                                                 'Voulez-vous changer les places à la table ?')

        if modifTable:
            for indexPlace in range(len(places)):
                joueurActif = places[indexPlace]
                places[indexPlace] = AttribuerPlace(joueurActif, indexPlace, regles)

        AfficherTable()

        dictTable['PHASE'] = 2

    #### PHASE 1 : MISES #########################################
    if dictTable['PHASE'] == 2:

        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE']:
                joueurActif['MISES']['DEPART'] = ChoisirMise(joueurActif, regles)
                joueurActif['CAPITAL'] -= joueurActif['MISES']['DEPART']

        dictTable['PHASE'] = 3

    # 3.Troisième boucle pour les mises optionnelles
    # TODO : Mises optionnelles ICI <<<

    #### PHASE 2 : DISTRIBUTION CARTES #########################################
    if dictTable['PHASE'] == 3:

        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE']:
                joueurActif['CARTES'].append(Piocher(sabot))
                joueurActif['SCORE'] = CalculerScore(joueurActif['CARTES'])
        banque['CARTES'].append(Piocher(sabot))
        # La première carte de la banque sera cachée !
        banque['SCORE'] = CalculerScore(banque['CARTES'])

        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE']:
                joueurActif['CARTES'].append(Piocher(sabot))
                joueurActif['SCORE'] = CalculerScore(joueurActif['CARTES'])
        banque['CARTES'].append(Piocher(sabot))
        banque['SCORE'] = CalculerScore(banque['CARTES'])

        AfficherTable()

        # 5. Cinquième boucle pour proposer l'assurance si la banque à un As en deuxième carte
        if banque['CARTES'][1][0] == 'A':
            for indexPlace in range(len(places)):
                joueurActif = places[indexPlace]
                if not joueurActif['LIBRE']:
                    if ProposerAssurance(joueurActif):
                        joueurActif['ASSURANCE'] = True
                        joueurActif['CAPITAL'] -= joueurActif['MISES']['DEPART']//2

            AfficherTable()

        dictTable['PHASE'] = 4

        #### Demande de sauvegarde de la phase en cours
        if DemanderSaisieBool('oui', 'non', 'Voulez-vous sauvegarder ?'):
            nomSave = DemanderSaisieStr(1,20,'Entrez le nom de la sauvegarde : ')
            SauvegarderTable(nomSave)

    #### PHASE 3 : TOURS DES JOUEURS #########################################
    if dictTable['PHASE'] == 4:

        AfficherTable()

        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE']:

                # Phase de split : on propose au joueur de Split s'il possède une paire éligible
                # Le split initial crée 2 nouveaux split dans la liste 'SPLIT' du joueur
                if ProposerSplit(joueurActif, joueurActif['CARTES']):
                    Splitter(joueurActif, joueurActif, 2)

                    # Si le joueur à Split au moins une paire, on résout son tour dans sa liste de Split interne
                    indexSplit = 0
                    while indexSplit < len(joueurActif['SPLIT']):
                        splitActif = joueurActif['SPLIT'][indexSplit]
                        splitActif['CARTES'].append(Piocher(sabot))
                        AfficherTable()

                        # Affichage temporaire de la carte du Split
                        print(f'{joueurActif['JOUEUR_NOM']}, split n°{indexSplit} : '
                              f'{splitActif['CARTES'][0]} et {splitActif['CARTES'][1]}')

                        if ProposerSplit(joueurActif, splitActif['CARTES']):
                            Splitter(splitActif, joueurActif, 1)
                            AfficherTable()
                        else:
                            # TOUR SPLIT
                            indexSplit += 1
                            if ProposerDouble(splitActif, joueurActif):
                                Doubler(splitActif, joueurActif)
                                splitActif['CARTES'].append(Piocher(sabot))
                                AfficherTable()
                                if VerifierScore(splitActif):
                                    DefausserCartes(splitActif['CARTES'], sabot)
                                    AfficherTable()

                            choixCarte = True
                            while choixCarte and not splitActif['BUST'] and not splitActif['DOUBLE']:
                                # Affichage temporaire du score
                                print(f'{joueurActif['JOUEUR_NOM']} : {splitActif['SCORE']}')

                                choixCarte = ProposerCarte(joueurActif)
                                if choixCarte:
                                    splitActif['CARTES'].append(Piocher(sabot))
                                    AfficherTable()
                                    if VerifierScore(splitActif):
                                        DefausserCartes(splitActif['CARTES'], sabot)
                                        AfficherTable()

                else:
                    # TOUR JOUEUR
                    choixCarte = True
                    if ProposerDouble(joueurActif, joueurActif):
                        Doubler(joueurActif, joueurActif)
                        joueurActif['CARTES'].append(Piocher(sabot))
                        AfficherTable()
                        if VerifierScore(joueurActif):
                            DefausserCartes(joueurActif['CARTES'], sabot)
                            AfficherTable()

                    while choixCarte and not joueurActif['BUST'] and not joueurActif['DOUBLE']:
                        choixCarte = ProposerCarte(joueurActif)
                        if choixCarte:
                            joueurActif['CARTES'].append(Piocher(sabot))
                            AfficherTable()
                            if VerifierScore(joueurActif):
                                DefausserCartes(joueurActif['CARTES'], sabot)
                                AfficherTable()
    dictTable['PHASE'] = 5

    #### PHASE 4 : TOUR DE LA BANQUE #########################################
    if dictTable['PHASE'] == 5:

        if banque['SCORE'] == 21:
            AfficherTable()
            for indexPlace in range(len(places)):
                joueurActif = places[indexPlace]
                if not joueurActif['LIBRE'] and joueurActif['ASSURANCE']:
                    joueurActif['ASSURANCE'] = False
                    joueurActif['CAPITAL'] += joueurActif['MISES']['DEPART'] // 2

        # 8. Tour de la Banque qui prend des cartes jusqu'à arriver à un score de 17+
        while banque['SCORE'] < 17 and not banque['BUST']:
            banque['CARTES'].append(Piocher(sabot))
            banque['SCORE'] = CalculerScore(banque['CARTES'])

        # 9. Huitième boucle pour comparer les scores des joueurs avec la banque et empocher leurs gains
        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE']:
                if len(joueurActif['SPLIT']) > 0:
                    for splitActif in joueurActif['SPLIT']:
                        if not splitActif['BUST']:
                            joueurActif['CAPITAL'] += ResultatMise(splitActif, banque)
                else:
                    if not joueurActif['BUST']:
                        joueurActif['CAPITAL'] += ResultatMise(joueurActif, banque)

    AfficherTable()

    time.sleep(5)

    dictTable['PHASE'] = 6

    #### PHASE 5 : FIN DE PARTIE #########################################
    if dictTable['PHASE'] == 6:

        # 10. Neuvième boucle pour terminer la partie : Ramasser les cartes, réinitialiser les variables du tour
        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE'] and not joueurActif['BUST']:
                # Ramassage des cartes des joueurs qui n'ont pas bust et de leurs splits
                if len(joueurActif['SPLIT']) > 0:
                    for split in joueurActif['SPLIT']:
                        if len(split['CARTES']) > 0:
                            DefausserCartes(split['CARTES'], sabot)
                joueurActif['SPLIT'] = []
                if len(joueurActif['CARTES']) > 0:
                    DefausserCartes(joueurActif['CARTES'], sabot)
        # Ramassage des cartes de la banque
        DefausserCartes(banque['CARTES'], sabot)

        # Réinitialisation des variables de raccourci avant les réinitialisations
        joueurActif = []
        splitActif = []

        # Boucle de réinitialisation pour chaque joueur
        for indexPlace in range(len(places)):
            joueurActif = places[indexPlace]
            if not joueurActif['LIBRE']:
                # Si le joueur n'a plus assez de Capital, on réinitialise sa place
                if joueurActif['CAPITAL'] < regles['TABLE_MISES'][0]:
                    joueurActif = ReinitialiserPlace()
                else:
                    # Réinitialisation des variables de tour
                    joueurActif['BUST'] = False
                    joueurActif['SCORE'] = 0
                    joueurActif['DOUBLE'] = False
                    joueurActif['MISES']['DEPART'] = 0

        # Réinitialisation des variables de la banque
        banque['SCORE'] = 0
        banque['BUST'] = False

        AfficherTable()

        # Si la carte d'arrêt a été révélée durant la partie, on remélange le sabot
        if sabot['ARRET']:
            sabot['PIOCHE'] = MelangerSabot(sabot['PIOCHE'] + sabot['DÉFAUSSE'])
            # Si le sabot n'est pas valide, on crée un nouveau sabot
            if not TesterIntegriteSabot(sabot):
                dictTable['SABOT']['PIOCHE'] = MelangerSabot(CreerSabot(dictTable['SABOT']['INFOS_CARTES']))
            # On place une nouvelle carte d'arrêt
            PlacerCarteArret(sabot['PIOCHE'])
            sabot['ARRET'] = False

    dictTable['PHASE'] = 1