informations = ["1e8t2h1a5n3.9si787l:v3854a@824o117u865t715l235o182o903k;7.e643s157","e*d9854en246.*m758e133y5748e5r@2439gm,8ai8533l.114c119o635m486","p412a=u2422l.%m!a959l%4l7et176@128y,o269p844m6497a2il=.740c393o436","k204e376n=8dj245i111.811m8875ey=2er741@391t931a9882i1ni383x3153.1ne;t637","t971i653a966g?o701.501b559o!n721n1365e8t@909y140o,p171m735a8441i7l3.6ne5523t","6e3t9h5an%.7809p2er8901r5ie302r9593@1ov1658h.982n612e296t503","9i6n8es2108.4le923c239l982e514r770q?5@9ao*l630.1346co632m?","l?i356n624a:.1264r4ou,s*s!4el5343@a587o1593l4.e3521u","i130n2973e3s.283m?5ey694e7589r@419g600o996o=g429l313e%9.e607u427","n728a402t9665h5a5n.697m=a977r524t9198i8n@903o444v1699h.635c5203o5m","a789n8662n4a.894l372e411c694l:3er152q8486@1yo288p452m4736a7il846.359b1563e","r?2ap3112h1ae159l9505.g794a=r:c7266i3a@%g!7oo219g760l217e9885.i647o457"]
choices = [8,9,5]
adressToKeep=[]
import string
alpha=list(string.ascii_lowercase)
alpha.append("@")
alpha.append(".")
num=[1,2,3,4,5,6,7,8,9]
result=[]
final=""
for chaine in informations:
    plop=list(chaine)
    depolue=plop.copy()
    for lettre in plop:    
        if lettre in num or lettre not in alpha:   
            depolue.remove(lettre)
    adress=''.join(depolue)
    result.append(adress)
            

for choice in choices:
    adressToKeep.append(result[choice])

final=",".join(adressToKeep)
print(final)









"""notes = ['Si', 'La', 'Fa', 'Mi', 'Do', 'Re', 'Sol']
music = 'Si,Si,Si,Re,Do,Si,Fa,Re,Si,Si,Fa,Mi,La'
result=[]
melodie=[]
final=""
nbNotes=music.count(",")
for i in range (nbNotes+1):
    melodie.append(music.split(",")[i])
    
for m in notes:
    nbNotesinMelodie=melodie.count(m)
    result.append(str(nbNotesinMelodie))

final=",".join(result)
print(final)





# NE PAS TOUCHER
kids = ["Lena_1","Martine_3","Guillaume_9","Anna_2","John_2","Mohamed_8","Christian_10","Rose_1","Amelie_3","Chloe_5","Pierre_10","Stephane_5","Manon_10","Martine_9","Pauline_8","Jules_10","Ines_9","Marie_1","Mael_7"]
fear = 6
time = 44
# NE PAS TOUCHER
result=""
for k in kids:
  if time>=3:
    if int(k.split("_")[1])<fear: 
        initiale=k.split("_")[0][0].upper()
        result=result+initiale
        time-=3
    else: 
        time-=5
    print(time)
   
if result=="":
    print("GRINCH")
else:
    print(result)





words = ['enserras', 'agnelage', 'groupera', 'minerais', 'assagies', 'geignard']
keys = [15, 24]
result=[]
import string
alpha=list(string.ascii_lowercase)
for word in words:
    new_word=""
    for lettre in word:
        idx=alpha.index(lettre)
        new_idx=(idx*keys[0]+keys[1])%26
        #print(idx, new_idx)
        new_word=new_word+alpha[new_idx]
    result.append(new_word)
final="-".join(result)
print(final)
"""