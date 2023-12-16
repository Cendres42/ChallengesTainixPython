# NE PAS TOUCHER
monsters = ["Luno19:2:2W8","Trex55:2:4R6","Vrip70:5:2G1","Plip66:1:4F4","Brux61:3:2F5","Fero45:5:2G6","Brop25:8:4R1","Drip11:7:2W2","Blit93:7:3W6","Fril94:7:4W1","Moki83:9:3F5","Grib31:9:4W8","Vexo13:9:4R6","Vexo60:1:2G6","Drex29:6:2W7","Brop12:5:4F6","Vrip20:2:2F6","Tiro69:6:3G1","Moki12:5:4R1","Plip62:1:3F1","Telo18:6:3G6"]
foods = "G9R2R5W4R5R6F8R4W2G7F3W5G2G1F5G4G9F4W7W9G6W7F9W5R7W6W8W9F9W3W2G3W9F5G8"
# NE PAS TOUCHER
monsters.sort()
foods=list(foods)

class Monstres():
    def __init__(self, monster):
        self.nom=monster[0:6]
        self.poids=int(monster[7])
        self.a=int(monster[9])
        self.L=monster[10]
        self.b=int(monster[11])

    # au print d'un objet str affiche la valeur de return
    def __str__(self):
        return f"{self.nom}:{self.poids}"

    def feed(self,P):
        new_p=self.poids+self.a*P+self.b        
        self.poids=new_p
tab_obj=[]        

for monster in monsters:
    objM=Monstres(monster) 
    tab_obj.append(objM)
#
# @brief Recherche le monstre le plus leger pour une lettre donnee
#
# @param lettre : La lettre recherchee
# @return integer : Index du monstre dans la liste monsters
#
def findMonster(lettre):
    min_p = 1000
    min_i = 1000
    # Parcours la liste de tous les monstres
    for idx in range(len(tab_obj)):
        monstre = tab_obj[idx]
        # Si et seulement si le montre a la lettre recherchee
        if monstre.L==lettre:
            # Alors, on extrait son poids
            p=monstre.poids
            # S'il est plus leger ...
            if p<min_p:
                # Alors on memorise son poids et sa position
                min_p = p
                min_i = idx
    return(min_i)
#
# @brief Change les poids de tous les objets monstres
#    
def changePoids():
    #parcours la liste de nourriture
    for i in range (0,len(foods),2):
        #récupère le poids de la nourriture
        P=int(foods[i+1])
        #on recherche l'index du monstre pour ce type de nourriture
        idx=findMonster(foods[i])
        #on récupère le monstre à cet index
        monstre=tab_obj[idx]
        # le monstre se nourrit et grossit
        monstre.feed(P)

#
# @brief Affiche le plus gros monstre après nourissage
#  
       
def printResult():
    temp=0
    x=0
    for m in tab_obj:
        if m.poids>temp:
            temp=m.poids
            x=m
    # appelle la méthode magique str pour le monstre x
    print(x)
    
#
# @brief Boucle principale
#  
def resolution():
    changePoids()
    printResult()

resolution()






