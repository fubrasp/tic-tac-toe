# -*- coding: utf-8 -*-
def print_liste(liste):
    print("")
    print("")
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            print(liste[i][j], end=' ')
        print()
    print("")
    print("")

# Double liste symbolisant le plateau de jeu
liste = [
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

joueur = 1
JetonsJoues = 0
P4 = False


#####################
# Fonctions

def quel_joueur():
    # Cette fonction retourne le numero du joueur qui doit jouer
    if (JetonsJoues % 2 == 0):
        jou = 1
    else:
        jou = -1
    return jou


def choisir_colonne(x, y):
    # Cette fonction retourne la colonne demandee au joueur1
    # Tant que la valeur n'est pas acceptable, on demande la colonne a jouer
    col = x - 16
    col = col / 97
    if col in range(0, 7):
        if (liste[5][int(col)] == 0):
            test = False
    return int(col)

def placer_pion(colonne):
    # boucle sur les lignes de bas en haut
    ligne=5 # par le bas 5 4 3 2 1 0
    #  ATTENTION CECI est different de l'encodage des pions. peut on utiliser true or false
    # False je continue, truej'arrete
    stop=False
    while ligne>=0 and stop==False:
        # si j'ai une case vide pour la colonne concernee
        if(liste[ligne][colonne]==0):
            if joueur == 1:
                # je mets mon pion jaune
                liste[ligne][colonne] = 1
                # vu que je viens de placer mon pion, je ne vais pas en placer d'autres.
                stop = True
            else:
                liste[ligne][colonne] = -1
                stop = True
        # je remonte de bas en haut avec colonne fixee dans liste
        ligne=ligne-1 # faire le parcours de bas en haut, parce que c'est plus performant (condition arret atteinte plus tot)



def gagnant_horizontal():
    # initialisation des variables
    # conserver le gagnant, vide si pas de gagnant
    gagnant=""
    # variable utilisee pour la boucle while
    ligne=5
    # variable qui sert a arret si on trouve le gagnant
    stop=False
    # raisonnement similaire, plus performant qu'un parcours traditionnel
    # on boucle tant qu'on n'a pas atteint (la ligne) 0 et que l'on a pas de gagnant
    # le while nous permet de nous deplacer dans les lignes de bas en haut (ligne 5 --> ligne 0)
    while ligne >= 0 and stop==False:
        for colonne in range (4): # ca nous permet deplacer dans les colonnes
            # pourquoi 4 ? 4 possibilites de gagner dans une ligne
            # on determine le gagnant en fonction des valeurs definies dans les 4 colonnes (que l'on decale grace a la variable colonne) que l'on regarde pour la ligne donnee i
            if liste[ligne][colonne] + liste[ligne][colonne+1] + liste[ligne][colonne+2] + liste[ligne][colonne+3] == 4 :#joueur jaune gagne
                # on affecte le gagnant (car on a nom nombre de points)
                gagnant="jaune"
                print(gagnant)
                # vu qu'on a gagne on arrete les parcours
                stop=True
            if liste[ligne][colonne] + liste[ligne][colonne+1] + liste[ligne][colonne+2] + liste[ligne][colonne+3] == -4 :#joueur rouge gagne
                gagnant="rouge"
                print(gagnant)
                stop=True
        # on remonte la ligne
        ligne=ligne-1
    # retourne la variable gagnant
    return gagnant

def gagnant_vertical():
	gagnant=""
# on regarde chaque colonne
	for colonne in range (7):
		# on descend les lignes pour la colonne concernee, pour verifier s'il y a un gagnant
		# tant que la ligne est strictement superieur a 2
		# 5 4 3 en baissant de -1 (3eme parametre du for)
		# c'est plus concis que ce qu'on a au-dessous
		for ligne in range(5, 2, -1):
			if liste[ligne][colonne] + liste[ligne-1][colonne] + liste[ligne-2][colonne] + liste[ligne-3][colonne] ==4:
				gagnant= "jaune"
			if liste[ligne][colonne] + liste[ligne-1][colonne] + liste[ligne-2][colonne] + liste[ligne-3][colonne] ==-4:
				gagnant= "rouge"
	return gagnant

def gagnant_diagonales():
	gagnant=""
	# on va diagonale d'en haut a gauche vers en bas a droite
	# on avance dans les lignes
	for ligne in range (3):
		# on avance dans les colonnes
		for colonne in range (4):
			# vu que c'est en meme on avance en diagonale
			if liste[ligne][colonne] + liste[ligne+1][colonne+1] + liste[ligne+2][colonne+2] + liste[ligne+3][colonne+3] == 4:
				gagnant = "jaune"
			if liste[ligne][colonne] + liste[ligne+1][colonne+1] + liste[ligne+2][colonne+2] + liste[ligne+3][colonne+3] == -4:
				gagnant = "rouge"
	# on va diagonale d'en haut a droite vers en bas a gauche
	for ligne in range (3):
		# 0 1 2 3, la ligne a laquelle on commence
		for colonne in range (3,7):
			# 3 4 5 6, on commence a la colonne 3 pour aller vers la 6
			if liste[ligne][colonne] + liste[ligne+1][colonne-1] + liste[ligne+2][colonne-2] + liste[ligne+3][colonne-3] == 4:
				gagnant = "jaune"
			if liste[ligne][colonne] + liste[ligne+1][colonne-1] + liste[ligne+2][colonne-2] + liste[ligne+3][colonne-3] == -4:
				gagnant = "rouge"
	return gagnant

def determiner_gagnant():
    # on verifie q'il gagnant d'abord horizontalement
    joueur = gagnant_horizontal()
    # s'il y a un gagnant, je n'ai pas besoin de verifier les autres cas
    # s'il n'y pas de gagnant je vais pas sur le return donc je peux continuer les autres etapes de la verification
    if (joueur != ""):
        return joueur
    joueur = gagnant_vertical()
    if (joueur != ""):
        return joueur
    joueur = gagnant_diagonales()
    if (joueur != ""):
        return joueur

# inutile c'est pour tester
def afficher_gagnant(joueur):
	if joueur =="" or joueur is None:
		return ("personne n'a gagne")
	else:
		return (joueur + " a gagne")

# Affichage du resultat
# j'affiche le retour de la methode afficger gagnant
print(afficher_gagnant(determiner_gagnant()))


# -*- coding: cp1252 -*-
import pygame
import sys

pygame.init()
image = pygame.image.load("plateau.png")
sizeim = image.get_size()
size = (sizeim[0] * 1, sizeim[1])
screen = pygame.display.set_mode(size)
screen.blit(image, (0, 0))
pygame.display.flip()

def extract_lines(liste):
    reversed_liste = []
    for row in range(5,-1,-1):
        reversed_liste.append(liste[row])
    return reversed_liste

def affichage():
    screen.fill((0, 0, 0))
    screen.blit(image, (0, 0))

    test = extract_lines(liste)

    print("DIPLAY")
    print_liste(test)

    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j] == 1:
                screen.blit(pionjaune, (16 + 97 * j, 13 - 97.5 * i + 486))
            pygame.display.flip()
            if test[i][j] == -1:
                screen.blit(pionrouge, (16 + 97 * j, 13 - 97.5 * i + 486))
            pygame.display.flip()


pionjaune = pygame.image.load("pion_jaune.png")
pionrouge = pygame.image.load("pion_rouge.png")
font = pygame.font.Font("freesansbold.ttf", 15)

import time

while (P4!="jaune" and P4!="rouge" and JetonsJoues < 42):
    time.sleep(0.1)
    # Le joueur joue
    for event in pygame.event.get():

        print_liste(liste)

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            joueur = quel_joueur()
            colonne = choisir_colonne(x, y)
            # On modifie les variables pour tenir compte du jeton depose.
            placer_pion(colonne)
            JetonsJoues = JetonsJoues + 1
            P4 = determiner_gagnant()
            affichage()
            pygame.display.flip()

        if event.type == pygame.QUIT:
            sys.exit()