time = 336
actions = 'BBBBBBBBBBBBBBBBBBBBBBBBBBBIIIIIIIIIIMMMMMEEEEEEEE'
references = 'B:8 I:6 M:2 E:7'
# NE PAS TOUCHER
tempsB= int(references[2])
tempsI= int(references[6])
tempsM= int(references[10])
tempsE= int(references[14])

for action in actions:
    if action=="B":
        time-=tempsB
    if action =="I":
        time-=tempsI
    if action=="M":
        time-=tempsM
    if action=="E":
        time-=tempsE
if time <=0:
    print(f"PRISON{abs(time)}")
else:
    print(f"ESCAPE{time}")
        
    