class Carte:
    def __init__(self, nom, mana, txt):
        self.__name = nom
        self.__mana = mana
        self.__description = txt

class Mage:
    def __init__(self, nom, main, defausse):
        self.__name = nom
        self.__pv = 100
        self.__manaMax = 80
        self.__mana = 50
        self.__tabDeck = main
        self.__tabDiscard= defausse
        #self.__gameZone = zone

    def getPv(self):
        return self.__pv
    def getMana(self):
        return self.__mana
    def getMain(self):
        return self.__tabDeck
    def getDefausse(self):
        return self.__tabDiscard

    def joueCarte(self): #ce qui la transfère de sa main à son jeu en payant de son mana
        self.__mana = self.__mana - 5        

    def recupererMana(self): #récupérer ses points de mana
        if self.__mana < self.__manaMax:
            recupereMana = self.__manaMax - self.__mana
            self.__mana = self.__mana + recupereMana
 
    def attaque(self,autreJoueur): #attaquer un-e autre Mage ou Creature avec une de ses Creatures en jeu
        autreJoueur.__pv = autreJoueur.__pv - 10

class Cristal(Carte):
    def __init__(self,valeur):
        self.__value = valeur
    
    def gagneManaTotal(self): # mana maximum augmente de sa valeur
        self.__manaMax = self.__manaMax + self.__value

class Creature(Carte):
    def __init__(self, pv, atk):
        self.__hp = pv
        self.__atk = atk
    
    def perdMana(self): #Peut être jouée (ce qui la place sur la zone de jeu du joueur) en payant son coût de mana
        self.__mana = self.__mana - 5

    def attaque(self,autreJoueur): 
        autreJoueur.__pv = autreJoueur.__pv - self.__atk

    def perdPv(self,autreJoueur): #peut perdre des points de vie, et même mourir
        self.__pv = self.__pv - autreJoueur.__atk
        if self.__pv <= 0:
            print("Navre... Vous etes mort.")

class Blast(Carte):
    def __init__(self, valeur):
        self.__value = valeur

    def enlevePv(self,autreJoueur): #enlève un nombre de points de vie égal à sa valeur
        autreJoueur.__pv = autreJoueur.__pv - self.__valeur

#Cartes
guerrier = Carte("Guerrier", 25, "Fort")
alchimiste = Carte("Alchimiste", 35, "Intelligent")
artisan = Carte("Artisan", 15, "Habile")

cristalRouge = Cristal(15)
cristalBleu = Cristal(10)
cristalVert = Cristal(5)

centaure = Creature(100,50)
licorne = Creature(100,30)
ogre = Creature(100,25)

atk_spe1 = Blast(70)
atk_spe2 = Blast(65)

joueur1 = Mage("Lisa",
               {1:guerrier, 2:alchimiste, 3:cristalBleu, 4:cristalRouge},
               {1:artisan, 2:cristalVert, 3:centaure, 4:atk_spe2})
joueur2 = Mage("Evelyne",
               {1:artisan, 2:cristalVert, 3:licorne, 4:ogre},
               {1:guerrier, 2:cristalRouge, 3:cristalBleu, 4:atk_spe1})

end = False
while(not end):
    choice = int(input("Quelle carte de votre main, souhaitez-vous utiliser [1,2,3,4] ?\n"))
    if choice == 1:
        joueur1.getMain()
        