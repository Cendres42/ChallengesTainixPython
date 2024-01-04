# NE PAS TOUCHER
planetes = ['WUM557:volcans 43:marais 11:deserts 68:champs 85:lacs 10:mers 63', 'WDA689:forets 43:jungles 80:lacs 62:plaines 26:canyons 81:grottes 56', 'HEB156:marais 33:champs 61', 'RQP792:forets 21:volcans 20:grottes 90:jungles 57:canyons 69:mers 85', 'ZGG562:montagnes 33:marais 61:volcans 38:champs 92:mers 95', 'LRP275:plaines 19:forets 89:champs 58', 'DUX551:jungles 97:canyons 17', 'PCL425:marais 54:deserts 53:champs 80:forets 58:grottes 55:lacs 65', 'QPE033:volcans 24:champs 40:grottes 56']
scores = 'marais 10:plaines 7:champs 10:montagnes 5'
# NE PAS TOUCHER

class Terrain():
    def __init__(self,infos):
        plop=infos.split(" ")
        self.nom=plop[0]
        self.prt=int(plop[1])

class Planete():
    def __init__(self,infos):
        plop=infos.split(":",1)
        self.code=plop[0]
        #passage par plop pour faire une liste avec la chaine retournée par split
        plop2=plop[1]
        liste_terrain=plop2.split(":")
        self.terrains=[]
        self.note=0
        for t in liste_terrain:
            new_ter=Terrain(t)
            self.terrains.append(new_ter)
       
    def __repr__(self):
        return(f"{self.code} ")
    
    def notation(self,tab_scores):
        note=0
        for i in range(len(self.terrains)):
            for elt in tab_scores:
                if self.terrains[i].nom == elt.nom:
                    note+=self.terrains[i].prt * elt.prt
        self.note=note
        return(self.note)


#creations des objets terrain et du tableau de scores
tab_scores=[]
t=scores.split(":")
for elt in t:
    new_s=Terrain(elt)
    tab_scores.append(new_s)

#creations des objets planete et du tableau de planetes
tab_planetes=[]
for p in planetes:
    new_p=Planete(p)  
    tab_planetes.append(new_p) 
noteM=0
for p in tab_planetes:
    noteP=p.notation(tab_scores)
    if noteP>noteM:
        noteM=noteP

if noteM==0:
    print("NOPLANET")
else:
    print(noteM)
