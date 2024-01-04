# NE PAS TOUCHER
ships = [9558,84,985,51,166,22,881,209,91,24,965,9018,65,73,77,854,1436,197,69,7280,40,42,93,2463,381,11,6515,74,276,807,58,95,6446,58,69,58,8071]
# NE PAS TOUCHER
p=0
puissanceT=0
import math
for i in range (len(ships)):
    resi =ships[i]
    if resi<100:
        p=math.ceil(resi/10)
    elif resi<1000:
        p=3*math.ceil(resi/100)+25
    elif resi<10000:
        p=5*math.ceil(resi/1000)+80
    puissanceT=puissanceT+p

print(puissanceT)






"""s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# on peut faire des opérations d'ensemble sur des sets
print(s1.union(s2)) # {1,2,3,4,5,6,7,8}
print(s1.intersection(s2)) # {4,5}
print(s1.difference(s2)) # {1,2,3}
print(s1.symmetric_difference(s2)) # {1,2,3,6,7,8}

# NE PAS TOUCHER
points = 'DDNDDNNDNNNNNNDDNNDDDNDNDNDDDNNDDDNNN'
RD=0
RN=0
jeuD=0
jeuN=0
setD=0
setN=0
for p in points:
    if p=="D":
        RD+=15
        if RD>45:
            jeuD+=1
            RD=0
            RN=0
            if jeuD>=6:
                setD+=1
                jeuD=0
                jeuN=0
    if p=="N":
        RN+=15
        if RN>45:
            jeuN+=1
            RN=0
            RD=0
            if jeuN>=6:
                setN+=1
                jeuD=0
                jeuN=0
    if RD==45:
        RD=40
    if RN==45:
        RN=40
    
print(f"{jeuD}:{jeuN}:{RD}:{RN}")
        



# NE PAS TOUCHER
planetes = ["KJQ123:pluvieux averses, tropical jungle","YAN552:pluvieux averses","WBO840:froid venteux","HRD893:froid venteux","NZW716:polaire glacial","OEM457:chaud fournaise","RHO781:chaud, tropical, tropical jungle","XOZ925:pluvieux averses","NEF656:polaire glacial","GIS372:pluvieux averses, froid, continental cool, froid venteux","ZUZ201:continental cool","FZZ220:polaire","VKN082:humide","OIS665:chaud","NXL425:tropical jungle","UMK595:pluvieux","KKW892:humide et moite, continental cool","OVW171:continental cool","ABE688:polaire glacial, continental cool, humide","YFN590:tropical jungle","DZX894:continental cool","WDB917:aride sans vie","OEE089:polaire glacial","PXP690:aride sans vie","OSB738:tropical"]
climat = "continental"
# NE PAS TOUCHER

result=""
dico={}
temp=""
for planete in planetes:
    dico[planete.split(":")[0]]=planete.split(":")[1]
#for valeur in dico.values():
for cle, value in dico.items():
    nb=value.count(',')
    for i in range(nb+1):
        climatP=value.split(', ')[i]
        if climatP==climat:
            temp=cle[0:3]
            result=result+temp
    if result=="":
        result="NOPLANET"
print(result)

 
 

        


# NE PAS TOUCHER
platforms = "P_____P___P____P_____P____P_P____P__P_P__P_P"
# NE PAS TOUCHER
result=""
liste=[]
trou=0
i=2
for p in platforms:
    liste.append(p)
#print(liste)
for elt in liste:
    if elt=='_':
        trou=trou+1
        
        
    elif elt=='P':
        if trou ==1 or trou==2:
            result=result+"M"
        elif trou ==4 or trou ==5:
            result=result+"P"
        elif trou==3:
            if i%2==0:
                result=result+"P"
            else:
                result=result+"M"
            i=i+1
        trou=0
print(result)
    
            


# NE PAS TOUCHER
decalage = -3
mot_crypte = 'zobsxppb'
# NE PAS TOUCHER
alpha="abcdefghijklmnopqrstuvwxyzabcdefghijkl"
code=""
for i in range(0,len(mot_crypte)):
    code=code+alpha[alpha.index(mot_crypte[i])-decalage]

print(code)

"""