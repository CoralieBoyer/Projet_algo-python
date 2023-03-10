import re
from ab import AB
from ab import ABlettre
# import pygame

def getIndex(abList, racine):
    for i in range(len(abList)): # On parcours la liste
        if abList[i].getRacine() == racine: # Si la racine de l'AB est égale à la racine de l'AB recherché
            return i # On retourne l'index de l'AB
    return -1


def readFile():
    fichier = open("arbre.txt", "r") # On ouvre le fichier en lecture
    ligne = fichier.readline()
    abList = []
    while ligne:
        infos = re.split('[(,)]', ligne) # On sépare les informations de l'arbre via une regex
        infos.pop()
        ab = AB(racine=infos[0]) # On crée un nouvel AB
        if infos[1] != "None":
            gauche = getIndex(abList, infos[1]) # Si il y a un AB à gauche, on récupère l'index de l'AB dans la liste
            if gauche != -1:
                ab.setGauche(abList[gauche]) # Puis on ajoute l'AB à gauche
        if infos[2] != "None":
            droite = getIndex(abList, infos[2]) # Si il y a un AB à droite, on récupère l'index de l'AB dans la liste
            if droite != -1:
                ab.setDroite(abList[droite]) # Puis on ajoute l'AB à droite
        abList.append(ab) # On ajoute le nouvel AB à la liste
        ligne = fichier.readline()
    fichier.close()
    return abList # On retourne la liste des AB


def sortList(abList, value):
    if len(abList)-1 == 0: # Si la liste ne contient qu'un seul élément
        if int(abList[0].getRacine()) <= int(value.getRacine()): # Si la valeur est plus grande que la valeur de l'AB
                abList.append(value) # On ajoute la valeur à la fin de la liste
        else:
            abList.insert(0, value) # Sinon on l'ajoute au début de la liste
    else:
        for i in range(len(abList)-1):  # On parcours la liste
            if int(abList[i].getRacine()) <= int(value.getRacine()) < int(abList[i+1].getRacine()): # Si la valeur est plus grande que la valeur de l'AB et plus petite que la valeur de l'AB suivant
                abList.insert(i+1, value) # On ajoute la valeur à la liste à l'index i+1
    return abList


def huffmanEncrypt(word):
    count = {} # Hashmap qui contient les lettres et leur nombre d'apparition
    for i in range(len(word)): # On parcours le mot et on ajoute les lettres dans le hashmap
        if word[i] in count:
            count[word[i]] += 1
        else:
            count[word[i]] = 1
    sortedCount = sorted(count.items(), key=lambda x: x[1], reverse=False) # On trie le hashmap par ordre croissant
    print(sortedCount)
    sortedABlettres = [] # Liste qui contient les ABlettre et AB triés par ordre croissant
    for i in range(len(sortedCount)): # On ajoute les ABlettre dans la liste
        sortedABlettres.append(ABlettre(racine=sortedCount[i][1], lettre=sortedCount[i][0]))
    while len(sortedABlettres) > 2: # Tant qu'il y a plus de valeurs dans la liste
        count = AB(racine=(int(sortedABlettres[0].getRacine()) + int(sortedABlettres[0].getRacine())), gauche=sortedABlettres[0], droite=sortedABlettres[1]) # On crée un AB avec les 2 premières valeurs de la liste
        sortedABlettres.pop(0) # On supprime les 2 premières valeurs de la liste
        sortedABlettres.pop(0)
        sortedABlettres = sortList(sortedABlettres, count) # On ajoute le nouvel AB dans la liste triée au bon endroit
    sortedABlettres[0] = AB(racine=(sortedABlettres[0].getRacine() + sortedABlettres[1].getRacine()), gauche=sortedABlettres[0], droite=sortedABlettres[1]) # On crée un AB avec les 2 dernières valeurs de la liste
    sortedABlettres.pop(1) # On supprime la dernière valeur de la liste
    sortedABlettres[0].prefixe() # On affiche le parcours prefixe de l'AB pour verifier que c'est bon

# Essaie de l'interface graphique
# def createTree(AB):
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     x, y = 400, 300
#     rayon = 50
#     pygame.draw.circle(screen, (255, 0, 0), (x, y), rayon)
#     pygame.display.flip()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()


def main():
    print("\n------Questions 1 à 6------")
    A1 = AB()
    print("A1 vide :", A1.estVide())
    A2 = AB(racine=5)
    print("A2 vide :", A2.estVide())
    A3 = AB(racine=3)
    A2.setGauche(A3)
    print("A2 gauche :", A2.getGauche())
    
    print("\n------Atest------")
    Atest3 = AB(racine=3)
    Atest8 = AB(racine=8)
    Atest5 = AB(racine=5, gauche=Atest3, droite=Atest8)
    Atest12 = AB(racine=12)
    Atest = AB(racine=10, gauche=Atest5, droite=Atest12)

    print("Atest vide :", Atest.estVide())
    print("Taille Atest :", Atest.taille())
    print("Question 10 : Oui cette méthode est récursive")
    print("Prefixe Atest :")
    Atest.prefixe()
    print("Infixe Atest :")
    print(Atest.infixe())
    print("Postfixe Atest :")
    Atest.postfixe()
    print("Hauteur Atest :", Atest.hauteur())
    print("Atest est un ABR :", Atest.estABR())

    print("\n------Partie2 (fichier)------")
    abList = readFile()
    abTest = abList[len(abList)-1]
    print("prefixe abTest :")
    abTest.prefixe()

    # createTree(AB=Atest)
    print("\n------Partie2 (Huffman)------")
    huffmanEncrypt("barbapapa")

    
if __name__ == "__main__":
    main()