# NE PAS TOUCHER
spells = ["Zyrifinimobiciatara","Colomotoviofinitrum","Legimusviodiyokeda","Endoductobadafli","Feraviokedafiadina","Omicurikoutrumcorpu","Riditumfiadina","Firiboumtumfini","Endolamategotrum","Nodiyofinipro","Difibadalegrapro","Ectocorpumusmus","Ulubadalimabadamoto","Flamfiafinicorpucuri","Oqutrumviowadilama","Colafinifiaboum","Omikedabadaciamusi","Zyriciataraveraytum","Flamcurivrafiacuri","Omikedalamadiyotrum"]
# NE PAS TOUCHER

voyelle=["a","e","i","o","u","y","A","E","I","O","U","Y"]
nbvoyelle=0
R=0
nbconsonne=0
for spell in spells:
    if spell[0] in voyelle:
        R=R+10
        print(spell[0])
    for lettre in voyelle:
        a=spell.count(lettre)
        nbvoyelle=nbvoyelle+a
    nbconsonne=len(spell)-nbvoyelle
    if nbconsonne>nbvoyelle:
        R=R+5
    elif nbconsonne==nbvoyelle:
        R=R+10
    elif nbconsonne<nbvoyelle:
        R=R+15
    print(nbvoyelle, nbconsonne,R)
    nbvoyelle=0
    nbconsonne=0
print(R)