class AB: #Création de la classe AB
    # Constructeur
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite
    
    # Setters et Getters
    def setRacine(self, racine):
        self.racine = racine

    def setGauche(self, gauche):
        self.gauche = gauche

    def setDroite(self, droite):
        self.droite = droite

    def getRacine(self):
        return self.racine
    
    def getGauche(self):
        return self.gauche
    
    def getDroite(self):
        return self.droite
    
    def __str__(self):
        return "AB(" + str(self.racine) + ", " + str(self.gauche) + ", " + str(self.droite) + ")"
    
    # Méthodes
    def estVide(self):
        return self.racine == None
    
    def taille(self): # Fonction récursive qui retourne la taille de l'arbre
        if self.estVide():
            return 0
        else:
            if self.gauche == None:
                tailleGauche = 0
            else:
                tailleGauche = self.gauche.taille()
            if self.droite == None:
                tailleDroite = 0
            else:
                tailleDroite = self.droite.taille()
            return 1 + tailleGauche + tailleDroite
        
    def prefixe(self): # Fonction récursive qui parcours l'arbre en commencant par la racine puis par la gauche et enfin par la droite
        if self.estVide():
            return
        print(self.racine)
        if self.gauche != None:
            self.gauche.prefixe()
        if self.droite != None:
            self.droite.prefixe()

    def infixe(self): # Fonction récursive qui parcours l'arbre en commencant par la gauche puis par la racine et enfin par la droite
        racine = ""
        if self.estVide():
            return
        if self.gauche != None:
            racine += str(self.gauche.infixe())
        racine += str(self.getRacine()) + " "
        if self.droite != None:
            racine += str(self.droite.infixe())
        return racine

    def postfixe(self): # Fonction récursive qui parcours l'arbre en commencant par la gauche puis par la droite et enfin par la racine
        if self.estVide():
            return
        if self.gauche != None:
            self.gauche.postfixe()
        if self.droite != None:
            self.droite.postfixe()
        print(self.racine)

    def hauteur(self): # Fonction récursive qui calcul la hauteur à gauche puis à droite et retourne la plus grande pour trouver la taille de l'arbre
        if self.estVide():
            return -1
        else:
            if self.gauche == None:
                hauteurGauche = -1
            else:
                hauteurGauche = self.gauche.hauteur()
            if self.droite == None:
                hauteurDroite = -1
            else:
                hauteurDroite = self.droite.hauteur()
            return 1 + max(hauteurGauche, hauteurDroite)
        
    def estABR(self): # Fonction récursive qui verifie si l'arbre est un ABR en vérifiant que le parcours infixe est croissant
        ab = self.infixe().split(" ")
        ab.pop()
        for i in range(len(ab)-1):
            if int(ab[i]) > int(ab[i+1]):
                return False
        return True
    
    def estEquilibre(self): # Fonction récursive qui verifie si l'arbre est équilibré en vérifiant que la différence (absolue) de hauteur entre la branche gauche et droite ne dépasse pas 1
        if self.estVide():
            return True
        if self.gauche == None:
            hauteurGauche = -1
        else:
            hauteurGauche = self.gauche.hauteur()
        if self.droite == None:
            hauteurDroite = -1
        else:
            hauteurDroite = self.droite.hauteur()
        if abs(hauteurGauche - hauteurDroite) > 1:
            return False
        if self.gauche != None:
            if not self.gauche.estEquilibre():
                return False
        if self.droite != None:
            if not self.droite.estEquilibre():
                return False
        return True 


class ABlettre (AB): # Création de la classe ABlettre qui hérite de la classe AB
    # Constructeur
    def __init__(self, racine=None, gauche=None, droite=None, lettre=None):
        super().__init__(racine, gauche, droite)
        self.lettre = lettre

    # Setter et Getter
    def setLettre(self, lettre):
        self.lettre = lettre

    def getLettre(self):
        return self.lettre