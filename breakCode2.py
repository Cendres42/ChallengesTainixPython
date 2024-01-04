letters = 'f4ik80x6lw2wpuh3es62qe54gu9dosc7cxxad0mndtay55ne0kvh55sewex3kf8zjvu8ewqwosc7cxxadjrv9dehq9ddb3inmosc7cxxadc60t55rf55gy7z6rxvifefuosc7cxxad51f6hky7veuk0v77zg1sb6ta2m3fg1pbu3rjyrosc7cxxadx5tswxv'
import math
max=math.floor((len(letters)/4))
dico={}
def findCode(t,ctr,maxi):
    for i in range(len(letters)):
        nb=letters.count(letters[i:i+t])
        nbL=len(letters[i:i+t])
        if nb>ctr and nbL>=8:
            ctr=nb 
            code=letters[i:i+t]
            dico[code]=len(letters[i:i+t])
        elif nb==ctr and nbL>=8:
            code=letters[i:i+t]
            dico[code]=len(letters[i:i+t])
            code=letters[i:i+t]
    #    print(letters[i:i+t])
    dico_ordered=sorted(dico.items(), key=lambda t: t[1],reverse=True)
    maxi=dico_ordered[0][0]
    return str(ctr)+"-"+maxi

temp=0
ctr=0
maxi=""
for t in range(8,max):
    if t==8:
        plop=findCode(t,ctr,maxi)
    elif t>8:
        plop= findCode(t,int(plop.split("-")[0]),plop.split("-")[1])
print(plop.split("-")[1].upper())
