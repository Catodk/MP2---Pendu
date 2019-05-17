from random import *
from turtle import *
import time

def choisirMOTpendu(): #cette fonction permet de prendre un mot hasard dans un fichier texte.

    global lmotadeviner #rend la variable mot globale, c'est à dire qu'on peut l'utiliser dans n'importe quelle fonction.

    motsFR=open("eng.txt", "r", encoding="utf8")
    mots=motsFR.readlines() #lis chaque ligne du fichier

    for i in mots:
        motadeviner=mots[randint(0,450000)] #choisis une ligne au hasard dans le fichier texte

    lmotadeviner=list(motadeviner) #transforme le mot en une liste de lettres
    lmotadeviner.pop() #supprime le dernier élément de la liste: le "ENTER"


def CreerJeuDepart():

    global lettresdevinees

    for i in range (len(lmotadeviner)):
        lettresdevinees.append("_") #crée le "_ _ _ _" pour afficher la longueur du mot etc.

    print(" ".join(lettresdevinees)) #affiche le pointillé sans les ' ou les []



def untourpendu():

    lettre=str(input('Pick a letter:')) #le joueur rentre une lettre

    for i in range (len(lettresdevinees)):
        if lmotadeviner[i]==lettre:
            lettresdevinees[i]=lettre #remplace le _ par la lettre si elle est correctement devinée

    if lettre not in lmotadeviner:
        print(lettre, "isn't in the word, try again hoe.") #si la lettre est faussement devinée, ceci est affiché
        dessindupendu() #dessine le bonhomme

    print(" ".join(lettresdevinees))



def tourspendu(): #mise en place du debut du jeu et verification de victoire/defaite

    tour=0 #nombre de tours au départ
    choisirMOTpendu() #choisis un mot au hasard
    CreerJeuDepart() #crée les pointillés

    while NbFautes<11 and '_' in lettresdevinees: #lorsque le bonhomme n'est pas pendu et que le mot n'est pas deviné
        untourpendu() #fait jouer le joueur
        tour=tour+1 #on rajoute un tour à chaque fois qu'on joue

    if '_' in lettresdevinees:
        print("Jayloser!!!!") #si à la fin de 11 fautes le mot n'est toujours pas complet, c'est perdu
    else:
        print("You won!!!!!!!!!") #sinon, c'est gagné
    print("Le mot était", "".join(lmotadeviner)) #le mot est affiché
    time.sleep(3)
    exit()
    
def jeudupendu():
    reset()
    tourspendu() #initialise le programme

lmotadeviner=[]
lettresdevinees=[]
NbFautes=0 #Nombre de fautes au départ


def dessindupendu():

    global NbFautes

    NbFautes=NbFautes+1 #augmente le nombre de fautes par 1 à chaque faute

    #recommence le pendu depuis le début (permet de ne pas emmêler les figures)

    if NbFautes==1: #dessine la barre en haut (1ère faute)
        up()
        goto(-200,200)
        down()
        forward(200)

    if NbFautes==2: #dessine la barre qui descend (2ème faute)
        left(180)
        forward(180)
        left(90)
        forward(300)

    if NbFautes==3: #dessine le socle (3ème faute)
        left(90)
        forward(50)
        left(180)
        forward(100)
        left(180)
        forward(50)
        left(90)

    if NbFautes==4: #dessine la barre qui tient (4ème faute)
        forward(250)
        right(45)
        forward(71)
        right(45)
        forward(100)

    if NbFautes==5: #dessine la corde (5ème faute)
        right(90)
        forward(80)

    if NbFautes==6: #dessine la tête (6ème faute)
        left(90)
        circle(20)

    if NbFautes==7: #dessine le bras droit (7ème faute)
        right(90)
        forward(15)
        left(90)
        forward(25)
        right(90)
        forward(50)

    if NbFautes==8: #dessine le bras gauche (8ème faute)
        left(180)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)

    if NbFautes==9: #dessine le tronc (9ème faute)
        left(180)
        forward(50)
        right(90)
        forward(25)
        right(90)
        forward(80)

    if NbFautes==10: #dessine la jambe droite (10ème faute)
        left(90)
        forward(12)
        right(90)
        forward(80)

    if NbFautes==11: #dessine la jambe gauche (11ème faute)
        left(180)
        forward(80)
        left(90)
        forward(25)
        left(90)
        forward(80)



jeudupendu()
