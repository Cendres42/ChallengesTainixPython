
# NE PAS TOUCHER
line1 = ["109:26","116:32","113:11"]
line2 = ["92:100","103:39","103:100","87:59"]
line3 = ["100:77"]
# NE PAS TOUCHER

import math
impactT1=0
impactT2=0
impactT3=0

for line in line1:
    poids=int(line.split(":")[0])
    #print(poids)
    force=int(line.split(":")[1])
    #print(force)
    impact1=math.floor(poids*force*1.5)
    impactT1=impactT1+impact1
    
#print("impact1", impactT1)

for line in line2:
    poids=int(line.split(":")[0])
    #print(poids)
    force=int(line.split(":")[1])
    #print(force)
    impact2=math.floor(poids*force)
    impactT2=impactT2+impact2
#print("impact2", impactT2)

for line in line3:
    poids=int(line.split(":")[0])
    #print(poids)
    force=int(line.split(":")[1])
    #print(force)
    impact3=math.floor(poids*force*0.75)
    impactT3=impactT3+impact3
#print("impact3",impactT3)
impactTT=impactT1+impactT2+impactT3
print(impactTT)
