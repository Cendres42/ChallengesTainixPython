queue_lezard = 13
oreille_souris = 7
petale_rose = 12
nuage_tenebreux = 11
poussiere_fee = 15
eau_jouvence = 10
bave_crapaud = 14


dico_acide={"queue_lezard" : 22, "oreille_souris": 27, "petale_rose" : 28}
dico_foudre={"nuage_tenebreux ": 28,"poussiere_fee" : 24}
dico_givre={"eau_jouvence" : 27,"bave_crapaud ": 20}

degats=0
potion_givre=0
potion_acide=0
potion_foudre=0
while queue_lezard>=3 and oreille_souris>=2 and petale_rose>=1:
    queue_lezard=queue_lezard-3
    oreille_souris=oreille_souris-2
    petale_rose=petale_rose-1
    potion_acide=potion_acide+1
#print(potion_acide)

while nuage_tenebreux>=2 and poussiere_fee>=1:
    nuage_tenebreux=nuage_tenebreux-2
    poussiere_fee=poussiere_fee-1
    potion_givre=potion_givre+1
#print(potion_givre)

while eau_jouvence>=3 and bave_crapaud>=1 :
    eau_jouvence=eau_jouvence-3
    bave_crapaud=bave_crapaud-1
    potion_foudre=potion_foudre+1
#print(potion_foudre)
degats=potion_acide*2+potion_givre*3+potion_foudre*1
print(degats)

       

