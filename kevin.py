pieges = ['A:3:6;9', 'C:3:1;8', 'Y:2:3;7', 'L:2:0;1']
parcours = 'DHHDHHHDHHDBBDDHDDHHHD'
vx=0
vy=0
seq=""
class Piege():
    def __init__(self,piege):
        self.type=piege[0]
        self.taille=int(piege[2])
        self.x=int(piege[4])
        self.y=int(piege[6])
tab_p=[]
def createPiege():
    for piege in pieges:
        new_p=Piege(piege)
        tab_p.append(new_p)
    tab_p.sort(key=lambda x:x.type)
    return tab_p


def parcourir():
    tab_p=createPiege()
    vx=0
    vy=0
    seq=""
    for o in parcours:
        if o=="D":
            vx+=1
            vy=vy
        elif o=="H":
            vy+=1
            vx=vx
        elif o=="B":
            vx=vx
            vy-=1
        seq=check_pos(seq,vx,vy)
    if seq=="":
        print("KEVIN")
    else:
        print(seq)

def check_pos(seq,vx,vy):
    for p in tab_p:
        if p.taille==3:
            if vx-p.x >=0 and vx-p.x<=2 and vy-p.y>=0 and vy-p.y<=2 :
                seq=seq+p.type
        elif p.taille==2:
            if vx-p.x >=0 and vx-p.x<=1 and vy-p.y>=0 and vy-p.y<=1 :
                seq=seq+p.type
        elif p.taille==1:
            if vx-p.x==0 and vy-p.y==0:
                seq=seq+p.type
        else:
            seq=seq
        #print(f" vx :{vx} vy:{vy} px:{p.x} py:{p.y} seq: {seq}")
    return seq
  

parcourir()
