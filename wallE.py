# NE PAS TOUCHER
force = 11
vitesse = 11
batterie = 95
dechets = [13,25,5,28,11,9,18,18,23,23,32,16,5,9,15,6,9,12,9,9]
# NE PAS TOUCHER

import math
prctbat=batterie
forceI=force
for poids in dechets:
    force=forceI
    compteur=0
    if force>=poids:
        prctbat=prctbat-1
        #dechets.remove(poids)
        print("glop",poids,prctbat,force)
    else:
        while force<poids:
            force+=1
            prctbat=prctbat-2
            compteur=compteur+2
            if prctbat<=0:
                prctbat=prctbat-2+compteur
                break
        if prctbat <20:
            if prctbat<vitesse:
                prctbat="KO"
                break
            else:
                prctbat=100-vitesse
                print(prctbat)
    print("plop",poids,prctbat,force)
      
print(prctbat)