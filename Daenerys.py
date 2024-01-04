# NE PAS TOUCHER
sac = 533
objets = [56,40,21,16,49,44,77,73,50,72,43,28,42,70,60,55,75,76,18,47,71,54,20,68,31,84,57,62,90,46,11,33,45,81,66,59,48,80,39,30,32,86,23,14,85,67,25,79,26,36,17,27,15,53,89,12]
# NE PAS TOUCHER
poids=0
objets.sort(reverse=True)
for i in range (10):
    if poids<=sac:
        poids=poids+objets[i]
        if poids>sac:
            poids=poids-objets[i]
            break
    else:
        break

objets.sort()
for i in range (10):
    if poids<=sac:
        poids=poids+objets[i]
        if poids>sac:
            poids=poids-objets[i]
            break
    else:
        break


print(poids)


    
    











"""
# NE PAS TOUCHER
shapes = ["pentagon_9","hexagon_7","hexagon_6","triangle_2","triangle_5","pentagon_9","triangle_9","hexagon_1","triangle_4","pentagon_7","pentagon_6","square_3","hexagon_9","pentagon_3","triangle_5","pentagon_9","triangle_9","triangle_5","hexagon_2","pentagon_2","square_3","triangle_4","hexagon_2","pentagon_2","hexagon_8"]
# NE PAS TOUCHER
perim=0
for shape in shapes:
    fig=shape.split("_")[0]
    if fig=="pentagon":
        nbC=5
    if fig=="hexagon":
        nbC=6
    if fig=="square":
        nbC=4
    if fig=="triangle":
        nbC=3
    lg=int(shape.split("_")[1])
    perim=perim+(nbC*lg)
print(perim)
    









# NE PAS TOUCHER
armee = 6901
# NE PAS TOUCHER

dragon=armee//3//1000
armee2=armee-dragon*1000
immac=armee2//2//15

armee3=armee2-immac*15
dot=armee3
print(f"{dragon}_{immac}_{dot}")
"""