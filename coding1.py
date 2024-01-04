# NE PAS TOUCHER
words = ["ULCSACUQTU","NICZYEXULI","VZPSHLOFLU","DJCSAYXEPU","VUESYXXJZU","NJCSABXFLU","NJCYSXQFLX","OYTWLYXZLC","SONSAYUFLU","NCXHKFXFLL","NUDSLHFFXU","PJCSAOXALU","NJCSACBIKU","NJCFTZDFLJ","NJCSQYXFQK","NJCSABXFLU","YJCSAWXFWU","LKCBXYSFCU","DUCSAYXQEL","YJCQAJXELU","NKMSAYXFLU","UVCSAQXFLU","NJVSFFXFUU","TACSARVYZQ","ZACKKYJFLU","RECCAPQSMD","PDCSTBFFAH","NFUYHICFLD","NUCUSYKZWU","NJZSAXXSLD","EOCSDYOGZU","NNCJAWLFLD","RGDSAMLKLR","NTCRFCXFYU","SZCDSYQBLL","NSMSTPDXLU","NGISNQXXIU","NJQBAYUCRU","ORZYARXWMU","AJASAYXRCU"]
# NE PAS TOUCHER

import string
alpha=list(string.ascii_uppercase)

class Mots():
    def __init__(self,infos):
        self.mot=infos

tab_mots=[]

def creationMots():
    for infos in words:
        mot=Mots(infos)
        tab_mots.append(mot)

def LettrePlace(numL):
    tab_lettre=[]
    for i in range(len(tab_mots)):
        tab_lettre.append(tab_mots[i].mot[numL])

    nb=0
    L=""
    for l in tab_lettre:
        nbL=tab_lettre.count(l)
        if nbL>nb:
            nb=nbL
            L=l
    return(L)


creationMots()
code="" 
for z in range(10):
    code=code+(LettrePlace(z))
print(code)








"""
# NE PAS TOUCHER
track = "R20_C51_T62_R89_O23_C75_T54_C87_O71_R95_C26_T49_C39_R33_S82_C42_R40_C80_R28_C79_O33_R97_C98_R29_S67"
delay = 132
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
    avance=132
    temps=0
    for tr in tab_track:
        if avance<=0:
            break
        else:
            if tr.obstacle=="R":
                gain=math.ceil(0.1*tr.value)
            elif tr.obstacle=="T":
                gain=5
            elif tr.obstacle=="C":
                gain=10
            elif tr.obstacle=="S":
                gain=math.ceil(0.5*tr.value)
            elif tr.obstacle=="O":
                gain=tr.value
            avance-=gain
            temps+=gain
    print(f"{tr.obstacle}{tr.value}:{temps}")

creation_obj()
calcul_vitesse()
"""