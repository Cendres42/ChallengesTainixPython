arts = ['Cosmos de Code #8', 'Reve de Donnees #8']
base = 30

from math import log
result=""
n=""
chaine=arts[0]
chaine2=arts[1]
for l in chaine:
   num=bin(ord(l))
   n=n+num[2:]

a1=2
a2=base

tz=['a','b','c','d','e','f']
ty=[]
tv=[]

def convert(n):
    L=int(log(n)/log(a2))
    s=int(n/(a2**L))
    N=n
    t3=[str(s)]
    while L>0:
        N-=(a2**L)*s
        L-=1
        s=int(N/(a2**L))
        t3.append(str(s))
    for u in range(0,len(t3)):
        if int(t3[u])>=10:
            t3[u]=chr(int(t3[u])+87)
    return t3

if a1<11:
    X=str(n)
    t=[]
    l=len(X)
    a=-1
    t1=[]

    while l>0:
        a+=1
        l-=1
        t1.append(int(X[a])*(a1**l))

    for i in range(0,len(X)):
        t.append(int(X[i]))
    if max(t)>=a1:
        print (" VOTRE NOMBRE N'EST PAS ECRIT EN BASE",a1,'!')
    else:
        firstPart="".join(convert(sum(t1)))

else:
    if " " in n:
        n=n.replace(" ","")
    for i in range(0,len(n)):
        ty.append(n[i])
    for i in range(0,len(ty)):
        if ty[i] in tz :
            ty[i]=str(ord(ty[i])-87)
    l=len(ty)-1
    a=0
    while l>-1:
        tv.append(int(ty[a])*(a1**l))
        l-=1
        a+=1

    firstPart="".join(convert(sum(tv)))

n=""
for l in chaine2:
   num=bin(ord(l))
   n=n+num[2:]

a1=2
a2=base

tz=['a','b','c','d','e','f']
ty=[]
tv=[]

def convert(n):
    L=int(log(n)/log(a2))
    s=int(n/(a2**L))
    N=n
    t3=[str(s)]
    while L>0:
        N-=(a2**L)*s
        L-=1
        s=int(N/(a2**L))
        t3.append(str(s))
    for u in range(0,len(t3)):
        if int(t3[u])>=10:
            t3[u]=chr(int(t3[u])+87)
    return t3

if a1<11:
    X=str(n)
    t=[]
    l=len(X)
    a=-1
    t1=[]

    while l>0:
        a+=1
        l-=1
        t1.append(int(X[a])*(a1**l))

    for i in range(0,len(X)):
        t.append(int(X[i]))
    if max(t)>=a1:
        print (" VOTRE NOMBRE N'EST PAS ECRIT EN BASE",a1,'!')
    else:
        secondPart="".join(convert(sum(t1)))

else:
    if " " in n:
        n=n.replace(" ","")
    for i in range(0,len(n)):
        ty.append(n[i])
    for i in range(0,len(ty)):
        if ty[i] in tz :
            ty[i]=str(ord(ty[i])-87)
    l=len(ty)-1
    a=0
    while l>-1:
        tv.append(int(ty[a])*(a1**l))
        l-=1
        a+=1

    secondPart="".join(convert(sum(tv)))

result=((firstPart)[0:10]+"_"+(secondPart)[0:10])
print(result)