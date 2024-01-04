# NE PAS TOUCHER
track = 'R37_O62_T49_O76_R68_S97'
delay = 42
# NE PAS TOUCHER

import math
class Track():
    def __init__(self,elt):
        self.obstacle=""
        self.value=0

tab_track=[]

def creation_obj(): 
    liste=track.split("_")       
    for elt in liste: 
        tr=Track(elt) 
        tab_track.append(tr)
        tr.obstacle=elt[0]
        tr.value=int(elt[1:])
        

def calcul_vitesse():
    avance=42
    temps=0
    for tr in tab_track:
        if avance >0 :
            if tr.obstacle=="R":
                gain=math.floor(0.1*tr.value)
            elif tr.obstacle=="T":
                gain=5
            elif tr.obstacle=="C":
                gain=10
            elif tr.obstacle=="S":
                gain=math.floor(0.5*tr.value)
            elif tr.obstacle=="O":
                gain=tr.value
            avance-=gain
            temps+=tr.value-gain
            if avance<=0:
                break
    print(f"{tr.obstacle}{tr.value}:{temps}")
creation_obj()
calcul_vitesse()
