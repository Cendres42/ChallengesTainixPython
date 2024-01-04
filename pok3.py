distance = 902
events = 'T_T__T__T__T__T__N_T'
duree=0
for i in range(len(events)):
    if events[i]=="T" and i==0 or i==len(events)-1:
        duree+=3600*5/50
        distance-=5
    elif events[i]=="T":
        duree+=(3600*5/50)*2
        distance-=5*2
    elif events[i]=="P":
        duree+=3600*10/5
        distance-=10
    elif events[i]=="N":
        duree+=3600*5/10
        distance-=5
    print(duree, distance)
duree+=3600*distance/200
print(duree)
    
        










"""# NE PAS TOUCHER
pokemons = ["Feu:19","Herbe:14","Feu:21","Psychique:71","Feu:33","Poison:73","Eau:45","Eau:34","Poison:86","Eau:46","Feu:38","Glace:47","Eau:25","Herbe:20","Herbe:50","Eau:27","Air:88","Psychique:26","Feu:49","Feu:42","Herbe:30","Poison:72","Air:91","Feu:38","Psychique:53","Insecte:90","Feu:19","Eau:40","Herbe:31","Eau:39","Psychique:62","Herbe:45","Feu:49","Feu:22","Herbe:14","Air:69","Eau:50","Eau:30","Herbe:24","Eau:24","Glace:79","Insecte:44","Feu:31","Eau:22"]
# NE PAS TOUCHER

class Pokemon():
    def __init__(self,p):
        plop=p.split(":")
        self.type=plop[0]
        self.force=int(plop[1])
tab_pokFeu=[]
tab_pokHerbe=[]
tab_pokEau=[]
tab_pokRares=[]
for p in pokemons:
    pok=Pokemon(p)
    if pok.type=="Feu":
        tab_pokFeu.append(pok)
    elif pok.type=="Herbe":
        tab_pokHerbe.append(pok)
    elif pok.type=="Eau":
        tab_pokEau.append(pok)
    else:
        tab_pokRares.append(pok)

tab_pokHerbe.sort(key=lambda x: x.force, reverse=True)
tab_pokEau.sort(key=lambda x: x.force, reverse=True)
tab_pokFeu.sort(key=lambda x: x.force, reverse=True)
tab_pokRares.sort(key=lambda x: x.force, reverse=True)

total=0
for i in range(3):
    total=total+tab_pokEau[i].force
    total=total+tab_pokFeu[i].force
    total=total+tab_pokHerbe[i].force
    total=total+tab_pokRares[i].force
print(total)
"""