# class Tirage pour récupérer chaque tirage de chaque game

class Tirage():
    def __init__(self,split_fin):
        self.vert=0
        self.bleu=0
        self.rouge=0
        self.resultat=0
        
tirage_sets=[]                  
# class game pour récupérer chaque ligne du fichier txt
class Game():
    def __init__(self,line):
        premier_split=line.split(":")
        # récupération des n tirages par jeu dans objet tirage
        listes_jeux=premier_split[1]
        des=listes_jeux.replace(";","")
        jeux=(des.replace(",","")).strip()
        split_fin=jeux.split(" ")
         # récupération du numéro de la game de chaque ligne
        prout=premier_split[0]
        self._numGame=int(prout.split()[1])
        #print(split_fin)
        #print(self.split_fin)
        tirage=Tirage(split_fin)
        tirage_sets.append(tirage)
        tempV=0
        tempR=0
        tempB=0
        for i in range(0,len(split_fin),2):
            nb_des=int(split_fin[i])
            clr_des=split_fin[i+1].strip()
            if clr_des=="blue" and tirage.bleu==0:
                tirage.bleu=int(nb_des)
                tempB=int(nb_des)
            elif clr_des=="blue" and int(nb_des)>tempB:
                tirage.bleu=int(nb_des)
                tempB=tirage.bleu
            if clr_des=="green" and tirage.vert==0:
                tirage.vert= int(nb_des)
                tempV=int(nb_des)
            elif clr_des=="green" and int(nb_des)>tempV:
                tirage.vert=int(nb_des)
                tempV=tirage.vert
            if clr_des=="red" and tirage.rouge==0:
                tirage.rouge=int(nb_des)
                tempR=int(nb_des)
            elif clr_des=="red" and int(nb_des)>tempR:
                tirage.rouge=int(nb_des)
                tempR=tirage.rouge
            tirage.resultat=tempR*tempV*tempB
      
        

    # affichage test numéros des games
    def __repr__(self):
        return(f"{self._numGame} ")
    
       



tab_game=[]
#
# @brief fonction qui lit chaque ligne et instancie objets games
#
def recupNombres2():
    file = open('C:/Users/Gwen/Desktop/Data/JeuxPython/advent2.txt', "r")
    line = file.readline()
    # Itérer sur les lignes
    while line:
        new_game=Game(line)
        tab_game.append(new_game)
        #print(new_game._sets)
        line = file.readline()
    file.close()

recupNombres2()
#
# @brief fonction d'addition des numéros des games dont les tirages sont valides
# @return affiche la somme de toutes les games valides
#
def theWinner():
    result=0   
    for tirage in tirage_sets:
        result=result+tirage.resultat
    print(result)

theWinner()
