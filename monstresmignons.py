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

tab_obj =[]

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
      
def changePoids():
    for i in range (0,len(foods),2):
        P=int(foods[i+1])
        #print("search letter ", foods[i])
        #if foods[i]=="W":
        minW=findMonster(foods[i])
        #print(minW)
        monstre=tab_obj[minW]
        new_p=monstre.poids+monstre.a*P+monstre.b        
        monstre.poids=new_p
        tab_obj[minW]=monstre
    temp=0
    x=0
    for t in tab_obj:
        if t.poids>temp:
            temp=t.poids
            x=t
    print(f"{x.nom}:{x.poids}")
changePoids()

for t in tab_obj:
    print(t.nom, ' ', t.poids)

def plop():
    #monster = monsters[minW]
    #pW = findLetter("W") 
    #pG= findLetter("G") 
    #pF= findLetter("F")
    #pR = findLetter("R")
    




    print(monsters)
    #findLetter("F")
    #findLetter("G")
    #findLetter("R")
    #print(monster)
"""  
import operator
dicoPW={}
dicoPR={}
dicoPG={}
dicoPF={}
dicoW={}
dicoG={}
dicoR={}
dicoF={}
liste=list(foods)
def bouclePoids(dico,dicoP):
     for cle, valeur in sorted(dicoP.items(),key=lambda t:t[0]):
            print(sorted(dicoP.items(),key=lambda t:t[0]))
            min_key = min(dicoP, key=dicoP.get)
            min_key = min(dicoP, key=dicoP.get)
            print(dicoP[min_key])    
            P=int(liste[i+1])
            a=int(dico[min_key][0])
            b=int(dico[min_key][2])
            dicoP[min_key]=dicoP[min_key]+a*P+b
            print(min_key,dicoP[min_key])




for monstre in monsters:
    if monstre[10]=="W":
        dicoPW[monstre.split(":")[0]]=int(monstre.split(":")[1])
        dicoW[monstre.split(":")[0]]=monstre.split(":")[2]
    if monstre[10]=="G":
        dicoPG[monstre.split(":")[0]]=int(monstre.split(":")[1])
        dicoG[monstre.split(":")[0]]=monstre.split(":")[2]
    if monstre[10]=="R":
        dicoPR[monstre.split(":")[0]]=int(monstre.split(":")[1])
        dicoR[monstre.split(":")[0]]=monstre.split(":")[2]
    if monstre[10]=="F":
        dicoPF[monstre.split(":")[0]]=int(monstre.split(":")[1])
        dicoF[monstre.split(":")[0]]=monstre.split(":")[2]

i=0
for i in range(len(liste)-1):
        if liste[i]=="W":
            bouclePoids(dicoW,dicoPW)
        if liste[i]=="G":
            bouclePoids(dicoG,dicoPG)
        if liste[i]=="R":
            bouclePoids(dicoR,dicoPR)
        if liste[i]=="F":
            bouclePoids(dicoF,dicoPF)

        i=i+2

dicoFinal={}
dicoFinal.update(dicoPR)
dicoFinal.update(dicoPW)
dicoFinal.update(dicoPG)
dicoFinal.update(dicoPF)

max_key = max(dicoFinal, key=dicoFinal.get)           
print(f"{max_key}:{max(dicoFinal.values())}") 














#print(poidsG+weight)
"""