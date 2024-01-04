ingredients = ['tomates:2', 'champignons:1', 'mozzarella:2', 'jambon:3', 'serrano:4', 'chevre:2', 'oeuf:3', 'chorizo:4', 'saumon:5', 'basilic:2', 'oignons:1', 'poivron:2', 'salade:1', 'anchois:2', 'olive:1', 'ananas:3']
pizzas = ['oignons,ananas,serrano,olive', 'tomates,oeuf,mozzarella,serrano,serrano,oignons', 'chorizo,jambon,basilic,tomates,anchois,tomates', 'salade,ananas,oeuf,salade,basilic,anchois', 'chorizo,poivron,anchois,oeuf', 'anchois,oeuf,oeuf,salade', 'mozzarella,tomates,mozzarella,serrano,jambon', 'basilic,anchois,oeuf,saumon,jambon,olive', 'tomates,chevre,serrano,tomates,basilic,basilic', 'champignons,anchois,chorizo', 'serrano,champignons,tomates,oignons', 'oignons,chorizo,saumon,chorizo,ananas', 'oeuf,oeuf,olive']
pizzaiolos = ['leonardo', 'michelangelo', 'michelangelo', 'michelangelo', 'donatello', 'michelangelo', 'raphael', 'donatello', 'michelangelo', 'leonardo', 'raphael', 'donatello', 'raphael']
dico={}

def donatello(i,dico):
    max=0
    prix=0
    for elt in pizzas[i].split(","):
        if dico[elt]>max:
            max=dico[elt]
    prix=max*5
    return prix
        
def leonardo(i,dico):
    prix=0
    for elt in pizzas[i].split(","):
        prix=prix+dico[elt]
    return prix

def michelangelo(i,dico):
    prix=0
    max1=0
    max2=0
    liste=pizzas[i].split(",")
    for elt in liste:
        if dico[elt]>max1:
            max1=dico[elt]
            Melt=elt
    liste.remove(Melt)
    for elt in liste:
        if dico[elt]>max2:
            max2=dico[elt]
    prix=(max1+max2)*3
    return prix

def raphael(i,dico):
    prix=0
    min=10
    max=0
    for elt in pizzas[i].split(","):
        if dico[elt]>max:
            max=dico[elt]
    for elt in pizzas[i].split(","):
        if dico[elt]<min:
            min=dico[elt]        
    prix=10+min+max
    return prix



prixF=0
for i in ingredients:
    plop=i.split(":")
    dico[plop[0]]=int(plop[1])

for i in range(len(pizzaiolos)):
    if pizzaiolos[i]=="donatello":
        prix=donatello(i,dico)
        prixF=prixF+prix
    elif pizzaiolos[i]=="leonardo":
        prix=leonardo(i,dico)
        prixF=prixF+prix
    elif pizzaiolos[i]=="michelangelo":
        prix=michelangelo(i,dico)
        prixF=prixF+prix
    elif pizzaiolos[i]=="raphael":
         prix=raphael(i,dico)
         prixF=prixF+prix
print(prixF)














# NE PAS TOUCHER
shots = [5, 5, 8, 2, 8, 4]
# NE PAS TOUCHER
p=0
for r in range(len(shots)):
    r=int(r)
    if r==0 or shots[r]>shots[r-1]:
        p=p+round((2*3.14*shots[r])*0.5,2)
    elif shots[r]<=shots[r-1]:
        p=p+round((2*3.14*shots[r])*1/3,2)
#print(round(p,2))

