dispositif = '3-4-3'
forces = [21, 9, 29, 28, 14, 16, 30, 5, 22, 17, 36, 39, 31, 10, 33, 12, 7, 34, 32, 35, 1]
postes = ['G', 'G', 'D', 'D', 'A', 'M', 'M', 'A', 'M', 'A', 'A', 'D', 'M', 'G', 'A', 'A', 'M', 'D', 'G', 'D', 'M']

tab_obj=[]
class Joueur():
    def __init__(self,poste,force):
        self._poste=poste
        self._force=force
        self._position=-1

    def __repr__(self):
        return (f"{self._position}")
    
    def setposition(self,pos):
        self._position=pos

def objJoueurs():
    for i in range(len(forces)):
        joueur=Joueur(postes[i],forces[i])
        joueur.setposition(i)
        tab_obj.append(joueur)

tab_equipe=[]
def meilleurGardien():
    for obj in tab_obj:
        if obj._poste=="G":
            tab_equipe.append(obj)
            break

def meilleursDef(lettre,nbDis):
    temp=[]
    result=""
    for obj in tab_obj:
        if obj._poste==lettre and len(temp)<int(dispositif[nbDis]):
            temp.append(obj)
            tab_equipe.append(obj)
    if len(temp)<int(dispositif[nbDis]):
        raise ValueError

def compoEquipe():
    objJoueurs()
    result=""
    tab_obj.sort(key=lambda x: x._force, reverse= True)
    meilleurGardien()
    meilleursDef("D",0)
    meilleursDef("M",2)
    meilleursDef("A",4)
    tab_equipe.sort(key=lambda x: x._force, reverse= True)
    #print(tab_equipe)    
    for j in tab_equipe:
        result=result+"-"+str(j._position)
    print(result[1:])

try:
    compoEquipe()
except :
    print("KO") 