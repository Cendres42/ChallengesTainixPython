force = 15
vitesse = 12
batterie = 79
dechets = [19, 22, 5, 7, 10]
import math
prctbat=batterie
forceI=force
for poids in dechets:
    bat=prctbat/2
    force=forceI
    compteur=0
    if force>=poids:
        prctbat=prctbat-1
        #dechets.remove(poids)
        #print("glop",poids,prctbat,force)
    else:
        while force<poids:
            force+=1
            prctbat=prctbat-2
            compteur=compteur+2
            if prctbat<=bat:
                prctbat=prctbat-2+compteur
                break
        if prctbat <20:
            if prctbat<vitesse:
                prctbat="KO"
                break
            else:
                prctbat=100-vitesse
                #print(prctbat)
    #print("plop",poids,prctbat,force)
      
print(prctbat)