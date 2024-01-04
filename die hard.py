# NE PAS TOUCHER
john = 54
ennemis = [72,87,65,73,86,57,91,59,64,78,69,60,41,43,61,40,44,48,94,96,66,68,75,58,82,88,76,85]
# NE PAS TOUCHER

class Ennemi():
    def __init__(self,etageI):
        self.etageI=etageI
        self.killed=False

def creationEnnemis():
    tab_ennemis=[]
    for ennemi in ennemis:
        new_en=Ennemi(ennemi)
        tab_ennemis.append(new_en)
        #print(new_en.etageI)
    #print(tab_ennemis)
    return tab_ennemis

tab_ennemis=creationEnnemis()
seq=str(john)
tab_ennemis.sort(key=lambda x: x.etageI)


i=0

while i <len(tab_ennemis):
    if tab_ennemis[i].etageI<john:
        i+=1
        continue
    else:
        etage=tab_ennemis[i].etageI
    if tab_ennemis[i].etageI == etage and tab_ennemis[i].killed==False:
        seq=seq+"-"+str(tab_ennemis[i].etageI)
        tab_ennemis[i].killed=True
        if i+1<len(tab_ennemis) and tab_ennemis[i+1].etageI <=etage+3 and tab_ennemis[i+1].killed==False:
            tab_ennemis[i+1].etageI-=1
        if i+2<len(tab_ennemis) and tab_ennemis[i+2].etageI<=etage+3 and tab_ennemis[i+2].killed==False:
            tab_ennemis[i+2].etageI-=1
        if i+3<len(tab_ennemis) and tab_ennemis[i+3].etageI<=etage+3 and tab_ennemis[i+3].killed==False:
            tab_ennemis[i+3].etageI-=1
    

    if i+1<len(tab_ennemis) and tab_ennemis[i+1].etageI== etage and tab_ennemis[i+1].killed==False:
        seq=seq+"-"+str(tab_ennemis[i+1].etageI)
        tab_ennemis[i+1].killed=True
        if i+2<len(tab_ennemis) and tab_ennemis[i+2].etageI<=etage+3 and tab_ennemis[i+2].killed==False:
            tab_ennemis[i+2].etageI-=1
        if i+3<len(tab_ennemis) and tab_ennemis[i+3].etageI<=etage+3 and tab_ennemis[i+3].killed==False:
            tab_ennemis[i+3].etageI-=1

    if i+2<len(tab_ennemis) and tab_ennemis[i+2].etageI ==etage and tab_ennemis[i+2].killed==False:
        seq=seq+"-"+str(tab_ennemis[i+2].etageI)
        tab_ennemis[i+2].killed=True
        if i+3<len(tab_ennemis) and tab_ennemis[i+3].etageI<=etage+3 and tab_ennemis[i+3].killed==False:
            tab_ennemis[i+3].etageI-=1

    if i+3<len(tab_ennemis) and tab_ennemis[i+3].etageI ==etage and tab_ennemis[i+3].killed==False:
            seq=seq+"-"+str(tab_ennemis[i+3].etageI)
            tab_ennemis[i+3].killed=True
        
    i+=1
seq=seq+"-"+str(100)
print(seq)


