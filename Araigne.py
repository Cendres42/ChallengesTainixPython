# NE PAS TOUCHER
flies = ['1;1:9:7', '2;2:9:4', '6;1:6:9', '3;1:5:4', '5;2:5:2', '7;4:3:4', '4;3:4:2', '8;2:3:1', '9;2:2:1', '10;3:0:2']# NE PAS TOUCHER

class Mouche():
    def __init__(self,infos):
        firstSplit=infos.split(";")
        self.id=int(firstSplit[0])
        secondSplit=firstSplit[1].split(":")
        self.taille=int(secondSplit[0])
        self.x=int(secondSplit[1])
        self.y=int(secondSplit[2])
        self.distance=0
        self.emballee=False

tab=[]
for f in flies:
    new_M=Mouche(f)
    tab.append(new_M)





def choixMouche(x,y):  
    for t in range(len(tab)):
        tab[t].distance=abs(tab[t].x-x)+abs(tab[t].y-y)
    tab.sort(key=lambda x:x.distance)
    for w in range(len(tab)):
        if tab[w].emballee==True:
            continue
        if w+1<len(tab):
            if tab[w].distance==tab[w+1].distance :
                if tab[w].id<tab[w+1].id or tab[w+1].emballee==True:
                    x=tab[w].x
                    y=tab[w].y
                    return w,x,y
                
                else:
                    x=tab[w+1].x
                    y=tab[w+1].y
                    return w+1,x,y
            else:
                x=tab[w].x
                y=tab[w].y
                return w ,x, y
        elif w==len(tab)-1:
            x=tab[w].x
            y=tab[w].y
            return w,x,y
        else:
            break

energie=80


def miam(energie,tab):
    x=0
    y=0 
    while True:
        w,x,y=choixMouche(x,y)
        #print(w,x,y)
        #print(energie, "avant marche, avant emballage")
        energie=energie-tab[w].distance
        #print(energie, "après marche, avant emballage")
        if energie>3*tab[w].taille:
            energie=energie-tab[w].taille*2
            tab[w].emballee=True
            #print(energie, "après emballage")
        else:
            for t in range(len(tab)):
                tab[t].distance=abs(tab[t].x-x)+abs(tab[t].y-y)
            tab.sort(key=lambda x:x.distance)
            for w in range(len(tab)):
                if tab[w].emballee==True:
                    energie=energie-tab[w].distance
                    x=tab[w].x
                    y=tab[w].y
                    energie=energie+5+(5*tab[w].taille)
                    #print(energie,"après repas",x,y)
                    break
        more=0
        for t in tab:
            if t.emballee==False:
                more=1
                break
        if (more==1):
            continue
        else:
            break
    return energie

energie=miam(80,tab)
print(energie)

