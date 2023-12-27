# NE PAS TOUCHER
map = [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1]
# NE PAS TOUCHER

import numpy as np
#construction matrice
def createMatColonne(a):
    tab=[]
    for i in range(a,225,15):
        tab.append(map[i])
    return tab

map_ar=[]

for i in range(15):
    tab=createMatColonne(i)
    map_ar.append(tab)
mat_arr=np.array(map_ar)
mat_array=mat_arr.T

def case(i,j,p):
    dessous=False
    if mat_array[i][j]==p:
        dessous=True
    else:
        dessous=False
    return dessous

def dessous(i,j,p):
    if mat_array[i+1][j]>=p :
        v=1
    else:
        v=0
    return v 

def dessus(i,j,p):
    if mat_array[i-1][j]>=p:
        v=1
    else:
        v=0
    return v

def gauche(i,j,p):
    if  mat_array[i][j-1]>=p:
        v=1
    else:
        v=0
    return v  

def droite(i,j,p):
    if j>=14:
        return 0
    if mat_array[i][j+1]>=p:
        v=1
    else:
        v=0
    return v 


def monterEtage(p):
    new_etage=0
    for i in range(len(mat_array)):
        for j in range(len(mat_array[i])):
            vDessous=0
            vDessus=0
            vGauche=0
            vDroite=0
            verif_dessous=case(i,j,p)
            if verif_dessous==True :
                vDroite=droite(i,j,p)
                if j>0:
                    vGauche=gauche(i,j,p)
                else:
                    vGauche=0
                if i<14:
                    vDessous=dessous(i,j,p)
                else:
                    vDessous=0
                if i>0:
                    vDessus=dessus(i,j,p)
                else:
                    vDessus=0

                v=vDroite+vGauche+vDessous+vDessus

                if v>=3:
                    mat_array[i][j]=p+1
                    new_etage+=1
            else:
                continue
    return new_etage
        

new_etage=1
p=1
while new_etage>0:
    valueF=new_etage
    new_etage=monterEtage(p)
    p=p+1
print(valueF*(p-1))
#print(mat_array)