# NE PAS TOUCHER
pokemons = ["Herbe:17","Feu:23","Eau:23","Psychique:66","Glace:82","Poison:37","Glace:90","Eau:15","Feu:15","Glace:94","Herbe:17","Psychique:34","Herbe:26","Herbe:11","Glace:94","Psychique:40","Feu:47","Insecte:46","Herbe:12"]
# NE PAS TOUCHER
pokEau=[]
pokHerbe=[]
pokFeu=[]
puissance=0
for pok in pokemons:
    value=pok.split(":")[0]
    force=pok.split(":")[1]
    if value=="Eau":
        pokEau.append(force)
    elif value=="Herbe":
        pokHerbe.append(force)
    elif value=="Feu":
        pokFeu.append(force)
pokEauMax=int(max(pokEau))
pokHerbeMax=int(max(pokHerbe))
pokFeuMmax=int(max(pokFeu))
puissance=pokEauMax+pokFeuMmax+pokHerbeMax

types_rares=["Air", "Poison", "Glace", "Psychique", "Insecte"]
temp=0
for pok in pokemons:
    type=pok.split(":")[0]
    if type in types_rares:
        force=int(pok.split(":")[1])
        if force>temp:
            temp=force
puissance=puissance+temp
            

#print(puissance)













# NE PAS TOUCHER
types = ["Eau","Glace","Eau","Psychique","Eau","Eau","Psychique","Herbe","Eau","Eau","Herbe","Eau","Feu","Psychique","Herbe","Feu","Eau","Feu","Psychique","Poison","Eau","Insecte","Feu","Glace","Feu","Insecte","Poison","Poison","Air","Insecte","Feu"]
# NE PAS TOUCHER
import math
types_bases=["Eau","Herbe","Feu"]
types_rares=["Air", "Poison", "Glace", "Psychique", "Insecte"]

dico_base={"Eau":0,"Feu":0, "Herbe":0}
dico_rares={"Air":0, "Poison":0, "Glace":0, "Psychique":0, "Insecte":0}

types=types.copy()
nb_pok=0
equipe=0
for type in types:
    if type in types_bases:
        dico_base[type]=dico_base[type]+1
        
    elif type in types_rares:
        dico_rares[type]=dico_rares[type]+1

for cle, valeur in dico_rares.items():
    equipe=min(dico_base.values())
    nb_pok=nb_pok+valeur
    if nb_pok>=equipe:
        equipe=equipe
    else:
        equipe=nb_pok



  














"""# NE PAS TOUCHER
ennemis = ["x:6 pv:114","x:14 pv:56","x:17 pv:28","x:13 pv:58","x:26 pv:67","x:9 pv:89","x:33 pv:49","x:12 pv:53","x:24 pv:51","x:15 pv:96","x:29 pv:10"]
# NE PAS TOUCHER
x=0
dico={}
value=""
feu=""
result=""
for ennemi in ennemis:
    tmp=ennemi.split(" ")
    #print(tmp)
    place=int(tmp[0].split(":")[1])
    pv=int(tmp[1].split(":")[1])
    dico[place]=pv   

for cle, valeur in sorted(dico.items(),key=lambda t:t[0]):
    position=cle-x
    x=cle
    points=valeur
    while points>0:
        feu=feu+"F"
        points=points-10
    
    for i in range(position):
        value=value+"D"
    result=result+value+feu
    value=""
    feu=""
print(result)



# NE PAS TOUCHER
group = ["HON","ALL","ESP","POL","DAN","UKR","TUR"]
scores = ["HON_ALL_0_2","HON_ESP_0_1","HON_POL_0_0","HON_DAN_2_3","HON_UKR_1_0","HON_TUR_1_2","ALL_HON_4_0","ALL_ESP_2_2","ALL_POL_1_1","ALL_DAN_2_1","ALL_UKR_1_2","ALL_TUR_0_0","ESP_HON_2_1","ESP_ALL_1_4","ESP_POL_3_4","ESP_DAN_0_3","ESP_UKR_0_3","ESP_TUR_0_4","POL_HON_0_0","POL_ALL_4_0","POL_ESP_1_0","POL_DAN_2_2","POL_UKR_0_0","POL_TUR_2_3","DAN_HON_2_0","DAN_ALL_0_0","DAN_ESP_1_1","DAN_POL_0_0","DAN_UKR_1_0","DAN_TUR_3_4","UKR_HON_1_2","UKR_ALL_0_3","UKR_ESP_1_1","UKR_POL_0_0","UKR_DAN_1_1","UKR_TUR_2_3","TUR_HON_2_0","TUR_ALL_0_1","TUR_ESP_3_0","TUR_POL_3_0","TUR_DAN_0_0","TUR_UKR_0_2"]
# NE PAS TOUCHER
dico={}
result=""
for g in group:
    dico[g]=0
#print(dico)
for score in scores:
    tmp=score.split("_")
    score1=tmp[2]
    score2=tmp[3]

    if score1<score2:
        pointEquipe1=0
        pointEquipe2=3
    elif score1>score2:
        pointEquipe1=3
        pointEquipe2=0
    else:
        pointEquipe1=1
        pointEquipe2=1

    dico[tmp[0]]+=pointEquipe1       
    dico[tmp[1]]+=pointEquipe2
    
for cle, valeur in sorted(dico.items(), key=lambda t: t[1],reverse=True):
    result=result+cle
print(result)
"""