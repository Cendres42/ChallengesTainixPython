allies = ['MRC_1', 'JMB_5', 'BGY_2', 'BOA_4']
enemies = ['SMK_7', 'KBY_1', 'MHK_3', 'GRP_4', 'AKU_9', 'KZR_8', 'AKJ_5']
force=3
class Allie():
    def __init__(self,infos):
        plop=infos.split("_")
        self.nom=plop[0]
        self.force=int(plop[1])
        self.use=False

class Ennemi():
    def __init__(self,infos):
        plop=infos.split("_")
        self.nom=plop[0]
        self.force=int(plop[1])

def createAllies():
    tab_A=[]
    for a in allies:
        new_a=Allie(a)
        tab_A.append(new_a)
        tab_A.sort(key=lambda x:x.force)
    return tab_A

def createEnnemis():
    tab_E=[]
    for e in enemies:
        new_e=Ennemi(e)
        tab_E.append(new_e)
    return tab_E

def searchAllie(chaine,e):
    nb=0
    v=0
    victoire=False
    for j in range(len(tab_A)):
        if tab_A[j].force+3>=e.force and tab_A[j].use==False:
            chaine=chaine+tab_A[j].nom+"_"
            tab_A[j].use=True
            victoire=True
            break
   
    return victoire, chaine




tab_A=createAllies()
tab_E=createEnnemis()
chaine=""
for e in tab_E:
    if e.force<=3:
        chaine=chaine+"LFY_"
    else:
        victoire,chaine=searchAllie(chaine,e)
        if victoire==False:
            chaine=chaine+"IVK"+"_"
print(chaine[:-1])   

