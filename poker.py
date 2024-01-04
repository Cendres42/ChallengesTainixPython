candidates = 'AVZWM'
votes = 'YZAVZKGZWAVZZVSSMZWGWZZWWZLAZWWAVZXWWKVAMVZZMZWZZMMMAVZVZVWZZWWMVWVVMWAMXWMMMYXXXXWWLVVJZVZAZVZWWAKKVVIWXWXWMMZS'

resultats={}
tab_c=[]
for c in candidates:
    tab_c.append(c)

tab_v=[]
for v in votes:
    tab_v.append(v)

votes_blancs=0
for v in tab_v:
    if v not in tab_c:
        votes_blancs+=1

votes_valables=len(tab_v)-votes_blancs


for l in tab_c:
    prt=round(votes.count(l)/votes_valables*100,1)
    resultats[l]=prt

ordered_result=sorted(resultats.items(),key=lambda t:t[1],reverse=True)


final=ordered_result[0][0]+str(ordered_result[0][1])+"-"+ordered_result[1][0]+str(ordered_result[1][1])
print(final)
















"""
mains = ['4 as 2 dame valet', 'as valet 4 10 10', '4 2 10 8 as', 'valet 9 9 9 valet', 'valet 6 9 7 roi', 'as dame valet 3 8', '3 7 9 5 3', '4 9 2 roi 7']

total=0
for elt in mains:
    liste_elt=elt.split(" ")
    nb=0 
    tab_nb=[]
    for l in liste_elt:
        nbL=liste_elt.count(l)
        tab_nb.append(nbL)
    if 4 in tab_nb:
        total=total+200
    elif 3 in tab_nb:
        if 2 in tab_nb:
            total=total+50
        else:
            total=total+20
    elif tab_nb.count(2)==4:
        total=total+10
    elif tab_nb.count(2)==2:
        total=total+5
    else:
        total=total+1
print(total)
        
          


"""