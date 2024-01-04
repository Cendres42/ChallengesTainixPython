sangoku = 'HP:10000 F:205 S:543'
vegeta = 'HP:10000 F:242 S:572'

s=sangoku.split(' ')
Sang_HP=int(s[0].split(":")[1])
Sang_Force=int(s[1].split(":")[1])
Sang_Special=int(s[2].split(":")[1])
v=vegeta.split(' ')
Veg_HP=int(v[0].split(":")[1])
Veg_Force=int(v[1].split(":")[1])
Veg_Special=int(v[2].split(":")[1])
Sang_C=0
Veg_C=0
nbT=0
nbCSVeg=0
nbCSang=0

while Sang_HP>0 and Veg_HP>0:
    
    nbT+=1
    if Sang_C<1000 and Veg_C<1000:
        Sang_HP-=Veg_Force
        Sang_C+=Veg_Force
        Veg_HP-=Sang_Force
        Veg_C+=Sang_Force
        #print(f"plop {Sang_HP} , {Veg_HP} , {Sang_C} , {Veg_C}" )
    elif Sang_C>=1000 and Veg_C>=1000:
        Sang_HP-=Veg_Special
        Veg_C=0
        nbCSVeg+=1
    elif Sang_C>=1000:
        Veg_HP-=Sang_Special
        Sang_C=0
        nbCSang+=1
    elif Veg_C>=1000:
        Sang_HP-=Veg_Special
        Veg_C=0
        nbCSVeg+=1
if Sang_HP<0 and Veg_HP<0:
    print(f"DRAW_{nbT}")
elif Sang_HP<0:
    print(f"VEGETA_{nbT}_{nbCSVeg}")
elif Veg_HP<0:
    print(f"SANGOKU_{nbT}_{nbCSang}")


    

















"""vehicles = ['Honda-Pilot_Ville_10_288', 'Mercedes-CClass_Campagne_5_256_IECC_EHRS', 'Porsche-Cayenne_Ville_12_768_IECC_EHRS', 'Ford-Ranger_Ville_9_274_IECC', 'Audi-A8_Campagne_7_461_EHRS', 'BMW-X5_Autoroute_12_965_EGR BP_IECC_EHRS', 'BMW-3Series_Campagne_9_787_IECC_EHRS', 'Toyota-Camry_Autoroute_11_638_EGR BP_IECC_EHRS', 'Ford-F150_Campagne_13_768', 'BMW-5Series_Ville_11_130_EGR BP_IECC_EHRS', 'Ford-Mustang_Autoroute_13_474', 'Mercedes-EClass_Autoroute_10_385_EGR BP_IECC_EHRS', 'Ford-F150_Campagne_11_882_IECC_EHRS']
import math
class Voiture():
    def __init__(self,infos):
        plop=infos.split("_")
        self.modele=plop[0]
        self.route=plop[1]
        self.conso=int(plop[2])
        self.distance=int(plop[3])
        self.eqpmts=plop[4:]

def createVoiture():
    tab_v=[]
    for v in vehicles:
        new_v=Voiture(v)
        tab_v.append(new_v)
    return tab_v

tab_v=createVoiture()
reduction=0
for voiture in tab_v:
    consoD=voiture.conso
    co2D=round(consoD/100*voiture.distance*2392)
    for e in voiture.eqpmts:
        if e=='EHRS':
            if voiture.route=="Ville":
                consoD=consoD*0.99
            if voiture.route=="Campagne":
                consoD=consoD*0.95
            if voiture.route=="Autoroute":
                consoD=consoD*0.96   
        elif e=='IECC':
            if voiture.route=="Ville":
                consoD=consoD*0.95
            if voiture.route=="Campagne":
                consoD=consoD*0.85
            if voiture.route=="Autoroute":
                consoD=consoD*0.93    
        elif e=='EGR BP':
            if voiture.route=="Ville":
                consoD=consoD*0.98
            if voiture.route=="Campagne":
                consoD=consoD*0.94
            if voiture.route=="Autoroute":
                consoD=consoD*0.96
        consoD=round(consoD,2) 
    co2F=round(consoD/100*voiture.distance*2392)
    reduction=reduction+co2D-co2F
print(math.floor(reduction))
      
"""