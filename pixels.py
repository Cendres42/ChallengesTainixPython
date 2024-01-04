meteorites = ['4:5#13', '6:5#29', '1:5#49', '3:3#10', '5:4#25', '0:3#30', '3:2#37', '0:1#32', '4:6#27']
instructions = 'RRTBBRLLLBLLRBRRLTLBTBTRLBLRTRRT'
starship = '4:3'

import math 
class Meteorite():
    def __init__(self,infos):
        plop=infos.split("#")
        coord=plop[0]
        coord=coord.split(":")
        self.taille=int(plop[1])
        self.x=int(coord[0])
        self.y=int(coord[1])

tab=[]
for m in meteorites:
    met=Meteorite(m)
    tab.append(met)


def mouvement(x,y):
    energie=verif(x,y)
    for i in range(len(instructions)):
        if instructions[i]=="R":
            x+=1
        if instructions[i]=="T":
            y+=1
        if instructions[i]=="B":
            y-=1
        if instructions[i]=="L":
            x-=1
        energieP=verif(x,y)
        energie+=energieP+1
        print("energie",energie)

    print(energie)
        

def verif(x,y):
    energie=0
    print("verif",x,y)
    for met in tab:
        if   y==met.y and((x-1)==met.x or (x+1)==met.x):
            energie+= math.ceil(met.taille/5) 
            print(x,y,met.x,met.y,energie, met.taille)
        elif x==met.x and ((y-1)==met.y or (y+1)==met.y):
            energie+= math.ceil(met.taille/5) 
            print(x,y,met.x,met.y,energie, met.taille)
       
    return energie

    


mouvement(4,3)

# NE PAS TOUCHER
map = ["r","r","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","r","w","w","w","r","w","w","w","w","w","w","w","w","w","w","r","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","r","w","r","r","w","w","r","w","r","w","r","w","w","w","w","r","w","w","w","w","w","r","w","r","w","w","w","r","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","r","w","w","r"]
# NE PAS TOUCHER
import numpy as np

def createMatL(a):
    tab=[]
    for i in range(a,100,10):
        tab.append(map[i])
    return tab
map_ar=[]

for i in range(10):
    tab=createMatL(i)
    map_ar.append(tab)
mat_arr=np.array(map_ar)
mat_array=mat_arr.T
#print(mat_array)

def dessous(i,j):
    if mat_array[i+1][j]=="r" or mat_array[i+1][j]=="b":
        v=0
    else:
        v=1
        mat_array[i+1][j]="b"
    return v 

def dessus(i,j):
    if mat_array[i-1][j]=="r" or mat_array[i-1][j]=="b":
        v=0
    else:
        v=1
        mat_array[i-1][j]="b"
    return v

def gauche(i,j):
    if  mat_array[i][j-1] =="r" or mat_array[i][j-1] =="b":
        v=0
    else:
        v=1
        mat_array[i][j-1] ="b"
    return v  

def droite(i,j):
    if mat_array[i][j+1]=="r" or mat_array[i][j+1]=="b":
        v=0
    else:
        v=1
        mat_array[i][j+1]="b"
    return v 

blue=0
for i in range(len(mat_array)):
    for j in range(len(mat_array[i])):
        c=mat_array[i][j]
        if c=='r':
            if i>=1 and i<=8 and j>=1 and j<=8:
                blue=blue+gauche(i,j)+droite(i,j)+dessous(i,j)+dessus(i,j)
            elif i==0  and j>=1 and j<9:
                blue=blue+gauche(i,j)+droite(i,j)+dessous(i,j)
            elif i==9 and j>=1 and j<9:
                blue=blue+gauche(i,j)+droite(i,j)+dessus(i,j)
            elif i==0 and j==0:
                blue=blue+droite(i,j)+dessous(i,j)
            elif i==0 and j==9:
                blue=blue+gauche(i,j)+dessous(i,j)
            elif i==9 and j==0:
                blue=blue+dessus(i,j)+droite(i,j)
            elif i==9 and j==9:
                blue=blue+dessus(i,j)+gauche(i,j)
            elif j==0 and i>=1 and i<9:
                blue=blue+dessous(i,j)+dessus(i,j)+droite(i,j)
            elif j==9 and i>=1 and i<9:
                blue=blue+dessous(i,j)+dessus(i,j)+gauche(i,j)
          
print(blue)
