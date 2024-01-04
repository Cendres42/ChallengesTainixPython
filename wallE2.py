# NE PAS TOUCHER
batterie = 89
cote = 5
dechets = ['2,4', '5,4', '2,6', '1,2', '2,5', '1,3']
chargeurs = ['4,6', '6,5']
# NE PAS TOUCHER
secu=cote*2

class Dechet():
    def __init__(self,infos):
        self.dechetX=int(infos[0])
        self.dechetY=int(infos[2])
        self.distance=self.dechetX-1+self.dechetY-1

class Chargeur():
    def __init__(self,infos):
        self.chargeurX=int(infos[0])
        self.chargeurY=int(infos[2])
        self.distance=self.chargeurX-1+self.chargeurY-1

#
# @ brief fonction qui initialise le tableau de déchets
# @ param la liste des déchets
# @ return le tableau de déchets
#
def initialisationDechets(dechets):
    tab_dechets=[]
    for d in dechets:
        new_d=Dechet(d)
        tab_dechets.append(new_d)
    return tab_dechets
#
# @ brief fonction qui initialise le tableau de chargeurs
# @ param la liste des chargeurs
# @ return le tableau de chargeurs
#
def initialisationChargeurs(chargeurs):
    tab_chargeurs=[]
    for c in chargeurs:
        new_c=Chargeur(c)
        tab_chargeurs.append(new_c)
        tab_dechets.sort(key=lambda x:x.distance)
    return tab_chargeurs
#
# @ brief calcul dela batterie nécessaire pour revenir avec le déchet et aller au suivant
# @ param le numéro du déchet, le niveau de batterie
# @ return le niveau de batterie obtenu après trajets
#
def calculBatterieNecessaire(i,batterie):
    if (i+1)<len(tab_dechets):
        batterieN=tab_dechets[i].distance*2+tab_dechets[i+1].distance
        batterieR=batterie-batterieN
    else: 
        batterieN=tab_dechets[i].distance*2
        batterieR=batterie-batterieN
    return batterieR
#
# @ brief fonction qui recharge WallE
# @ param le niveau de batterie, le tableau des chargeurs et des déchets
# @ return le niveau de batterie obtenu après recharge

def recharge(batterie,tab_chargeurs,tab_dechets,i,wallX,wallY):
    for t in tab_chargeurs:
        t.distance=abs(t.chargeurX-tab_dechets[i].dechetX) + abs(t.chargeurY-tab_dechets[i].dechetY)
    tab_chargeurs.sort(key=lambda x:x.distance)
    print("cx",tab_chargeurs[0].chargeurX,"wx",tab_dechets[i].dechetX, "cy",tab_chargeurs[0].chargeurY, "wy",tab_dechets[i].dechetY)

    retour=abs(tab_chargeurs[0].chargeurX-wallX)+abs(tab_chargeurs[0].chargeurY-wallY)
    batterie=100-retour
    print("glop",wallX,wallY,retour,batterie)
    return batterie


#programme principal
# initialisation des objets, récupération des 2 tableaux
tab_dechets=initialisationDechets(dechets)
tab_chargeurs=initialisationChargeurs(chargeurs)
for i in range(len(tab_dechets)):
    # WallE part des coodonnées (1,1)
    wallX=1
    wallY=1
    # aller à un déchet coute la distance en batterie
    batterie-=tab_dechets[i].distance
    wallX=tab_dechets[i].dechetX
    wallY=tab_dechets[i].dechetY
    print(wallX,wallY,batterie)
    # vérification batterie restante après gestion déchet et aller au suivant
    batterieR=calculBatterieNecessaire(i,batterie)
    # si niveau insufisant => recharge de la batterie
    if batterieR<secu:
        batterie=recharge(batterie,tab_chargeurs,tab_dechets,i,wallX,wallY)
        batterie-=tab_dechets[i].distance*2
    #si niveau seffisant retour au départ avec déchet et baisse batterie
    else:
        batterie-=tab_dechets[i].distance*2
    print(batterie)
#niveau de batterie final après traitement denier déchet:
print(batterie)


blocs = 'UUUUUUUSSSSSHHEEEEEEEEEBBBBBBBBCCCUUUUUUSSSSHHHHHHEEEEEEBBBBBBBBBCCCCCCCCCUUUUUUSSSSSHHHHHEEEEEEEBBBBCCCCCCCCCUUUUUUUUSS'

def compteur():
    i=0
    chaine=""
    while i+1<len(blocs):
        ctr=1
        while i+1<len(blocs) and blocs[i+1]==blocs[i]:
            ctr+=1
            i=i+1
        if ctr%2!=0:
           chaine=chaine+blocs[i-1]
        i=i+1
        print("compteur",ctr,"i",i)
    print(chaine)
compteur()           


