
islandX = 24
islandY = 52
planes = ["P:18,7C:TDT","P:78,99C:OGQ","P:97,13C:WZF","P:10,2C:PUS","P:91,1C:MYZ","P:36,10C:NOU","P:81,98C:RGW","P:89,67C:KEK","P:59,99C:ICT","P:17,9C:GMH"]
# NE PAS TOUCHER
import math

tab_dis=[]
#
# @ brief créaton class Avion pour conversion planes en tableau d'objets
#
class Avion():

    def __init__(self,plane):
        args=plane.split(",")
        self.x=int(args[0].strip("P:"))
        self.y=int(args[1][:-5])
        self.code=args[1][-3:]
        self.distance=0
    #
    # @brief calcule les distances de chaque avion 
    # utilisation théorème de Pythagore
    #
    #passer coordonnées en paramètres pour éviter dépendance avec variables externes
    def calculeDistances(self,X,Y):
        distanceX=abs(X-self.x)*abs(X-self.x)
        distanceY=abs(Y-self.y)*abs(Y-self.y)
        distance=(round(math.sqrt(distanceX+distanceY),2))
        self.distance=distance
        return self.distance
    
    # par ex au print d'un tableau d'objets repr affiche la valeur de return
    def __repr__(self):
        return self.code
    
    # au print d'un objet str affiche la valeur de return
    def __str__(self):
        return self.code
    
# création tableau d'objets avions
    
tab_obj=[]
for plane in planes:
    avion=Avion(plane)
    tab_obj.append(avion)
#
# @brief récupération 3 plus petites distances des avions
#
def recup3Distances():
    sauveurs=""
    #calcule distance des avions
    for avion in tab_obj:
        avion.calculeDistances(islandX,islandY)  
    #tri tableau selon distances
    tab_obj.sort(key=lambda x: x.distance)
    for i in range(3):
        #création chaine avec codes avion selon distances
        sauveurs=sauveurs+tab_obj[i].code
    print(sauveurs)
    print(tab_obj[0:3].strip(","))
recup3Distances()





      




    


    







"""
# NE PAS TOUCHER
names = ["Beatrice","Marie","Manon","Julia","David","Mila","Jack","Paul","Louis","Kim","Raphael","Mia","Louise","Pierre"]
x = -3
y = -5
moves = ["y:8","x:2","x:3","y:5","y:2","x:8","y:2","y:-7","y:3","y:-1","x:6","y:0","x:0","x:4","x:7","y:8","y:-2","y:-8","x:1","x:8","x:6","y:1","x:6","y:1"]
# NE PAS TOUCHER

message="SOS:"
message2=""
for name in names:
    message2=message2+name[0]
message=message+message2+"_"+"PLACE:"
for move in moves:
    moveLettre=move.split(":")[0]
    moveCases=int(move.split(":")[1])
    #print(moveLettre,moveCases)
    if moveLettre=="y":
        y=y+moveCases
    
    if moveLettre=="x":
        x=x+moveCases
    
message=f"{message}{x};{y}"
print(message)
"""