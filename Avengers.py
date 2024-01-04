# NE PAS TOUCHER
ironman = 7
spiderman = 5
captainamerica = 9
thor = 7
thanos = 138
# NE PAS TOUCHER

liste=[]
liste.append(ironman)
liste.append(spiderman)
liste.append(captainamerica)
liste.append(thor)

total=ironman*3+10+spiderman*4+5+captainamerica*3+7+thor*4+20
victoire=False
print(total)
compteur=1
while victoire==False:
    for i in range(4) :
        if total<=thanos:
            #print(i)
            liste[i]+=1
            #print(liste[i])
            total=liste[0]*3+10+liste[1]*4+5+liste[2]*3+7+liste[3]*4+20
            #print(total)
            compteur+=1
        else :
            victoire=True
            break
            

