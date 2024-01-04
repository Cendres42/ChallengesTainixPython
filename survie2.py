
thirst = 13
hunger = 14
shape = 63
island = ['AF__TFRFWFFFR', 'WAEFTTW', 'WWFWFWTAWW', 'YTFFZFFW_', 'AFZWFWFZRY', 'WWZYZYFWW', 'WR_EWEZWAZ']

# NE PAS TOUCHER
import math
result=0
liste=[]
for ile in island:
        for lettre in ile:
            if thirst <=0 or hunger<=0 or shape<=0 :
                print("break")
                break
            if thirst >0 and hunger>0 and shape>0 :
                shape-=1
                if lettre=="W":
                    thirst+=1
                if lettre=="F":
                    hunger+=1
                if lettre=="_":
                    shape-=2
        if thirst >0 and hunger>0 and shape>0 :
            print(shape,thirst,hunger,result)    
            shape=math.floor(shape+((thirst+hunger)/2))
            hunger-=5
            thirst-=5
if thirst<=0 :
    thirst=1
if hunger<=0 :
    hunger=1
if shape<=0 :
    shape=1
result=shape*hunger*thirst
print(result)










"""
result=0
compteur=0
suite=True
for ile in island:
        for lettre in ile:
            if thirst >0 and hunger>0 and shape>0 and suite==True:
                shape-=1
                if lettre=="W":
                    thirst+=1
                elif lettre=="F":
                    hunger+=1
                elif lettre=="_":
                    shape-=2
            if thirst>0 and hunger>0 and shape>0:
                result=thirst*hunger*shape
            elif suite==True: 
                if thirst<=0 and hunger!=0 and shape!=0:
                    result=hunger*shape
                    
                elif hunger<=0 and thirst!=0 and shape!=0:
                    result=thirst*shape
                    
                elif shape<=0 and thirst!=0 and hunger!=0:
                    result=thirst*hunger
                    
                elif thirst<=0 and hunger<=0:
                    result=shape
                elif thirst<=0 and shape<=0:
                    result=hunger
                elif hunger<=0 and shape<=0:
                    result=thirst
                #print(result) 
                suite=False
                break 
        print(thirst,hunger,shape) 
        shape=math.floor(shape+((thirst+hunger)/2))
        hunger-=5
        thirst-=5
print(result)
"""