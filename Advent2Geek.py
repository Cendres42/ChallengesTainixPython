
class Tirage():
    def __init__(self,jeu):
        self.split_des=jeu.split(",")
        self.vert=0
        self.bleu=0
        self.rouge=0
        for elt in self.split_des:
            x=elt.strip()
            y=x.split(" ")
            nb_des=y[0]
            clr_des=y[1]
            if clr_des=="blue":
                self.bleu+=int(nb_des)
            if clr_des=="green":
                self.vert+=int(nb_des)
            if clr_des=="red":
                self.rouge+=int(nb_des)

class Game():
    def __init__(self,line):
        premier_split=line.split(":")
        #
        liste_jeux= premier_split[1].split(";")
        self._sets=[]
        for jeu in liste_jeux:
            tirage=Tirage(jeu)
            self._sets.append(tirage)
        #
        prout=premier_split[0]
        self._numGame=int(prout.split()[1])

    def __repr__(self):
        return(f"{self._numGame} ")
    
    def isvalid(self,red,green,blue):
        for tirage in self._sets:
            if tirage.vert>green:
                return False
            if tirage.bleu>blue:
                return False
            if tirage.rouge>red:
                return False
        return True

    def getPower(self):
        blue  = -1
        green = -1
        red   = -1
        # Recherche les valeurs max parmis tous les tirages
        for tirage in self._sets:
            if (tirage.rouge > red):
                red = tirage.rouge
            if (tirage.vert > green):
                green = tirage.vert
            if (tirage.bleu > blue):
                blue = tirage.bleu
        # Calcul et renvoi le produit des trois couleurs
        return blue*red*green




tab_game=[]

def recupNombres2():
    file = open('C:/Users/Gwen/Desktop/Data/JeuxPython/advent2.txt', "r")
    line = file.readline()
    # Itérer sur les lignes
    while line:
        new_game=Game(line)
        tab_game.append(new_game)
        #print(new_game._sets)
        #print(tirage[0].find("red")-2)
        line = file.readline()
    file.close()

recupNombres2()

def theWinner():
    result=0   
    red=12
    green=13 
    blue=14
    for game in tab_game:
        result_game=game.isvalid(red,green,blue)
        if result_game==True:
            result+=game._numGame
    print(result)

def theWinnerPart2():
    result=0   
    for game in tab_game:
        result += game.getPower()
    print(result)


theWinnerPart2()