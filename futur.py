depart = 1985
anniversaire = '03-28'
sauts = ['1992-05-26', '1973-02-03', '2009-03-28', '1998-07-04', '1971-08-04']
mois=int(anniversaire[0:2])
jour=int(anniversaire[3:6])
#print(mois,jour)
class Saut():
    def __init__ (self, infos):
        to_set=infos.split("-")
        self.annee=int(to_set[0])
        self.mois=int(to_set[1])
        self.jour=int(to_set[2])

def createSauts():
    tab_sauts=[]
    for elt in sauts:
        saut=Saut(elt)
        tab_sauts.append(saut)
    return tab_sauts

def findMoisAvant(elt,nbA):
    if elt.mois<mois:
        nbA=nbA
    elif elt.mois==mois and elt.jour<jour:
        nbA=nbA
    else:
        nbA=nbA+1
    #print("avant",nbA)
    return nbA
    
def findMoisApres(elt,nbA):
    if elt.mois>mois :
        nbA=nbA
    elif elt.mois==mois and elt.jour>=jour:
        nbA=nbA
    else:
        nbA=nbA-1
    #print("après",nbA)
    return nbA

tab_sauts=createSauts()

def nb_annee(tab_sauts):
    nbA=0
    nbT=0
    for elt in tab_sauts:
        nbA=elt.annee-1985
        if nbA<0:
            nbA=findMoisAvant(elt,nbA)
        elif nbA>0:
            nbA=findMoisApres(elt,nbA)
        nbT=nbT+nbA
        #print(nbT)
    return nbT

nbT=nb_annee(tab_sauts)
print(nbT)

