cours = ['TTEE', 'DTET', 'PEPT', 'ETTT', 'PEPE', 'ETPT', 'PTTT', 'EETE', 'ETTE', 'TPEP', 'PEDP', 'TDPE', 'DEET', 'PEDT', 'TTPT', 'PEPT']

class Eleve():
    def __init__(self,infos):
        self.cpmt=infos


def createEleve(i):
    tab=[]
    for c in cours:
        tab.append(c[i])
        new_e=Eleve(tab) 
    return new_e

tab_classe=[] 
for i in range(len(cours[0])) :
    new_e=createEleve(i)
    tab_classe.append(new_e)
    

def noteEleve(eleve):
    note=12
    max=20
    for l in eleve.cpmt:
        if l=="E" or l=="T":
            note+=1
        elif l=="P":
            note-=1
            max-=1
        elif l=="D":
            note-=2
            max-=2
        if max<10:
            max=10
        if note<0:
            note=0
        if note>max:
            note=max
    print(note)
    return note

total=0
for e in tab_classe:
    #print(e.cpmt)
    note=noteEleve(e)
    total=total+note
    moyenne=total/len(cours[0])
print(round(moyenne,1))





"""objets = ['PERIZSP-274', 'LYQLXCC-552', 'NBTODZTNB-307', 'VWZFVEW-386', 'ACBYUTSR-237', 'JFNPTVGSPW-138', 'MSNNNUUTK-164', 'VZAEJA-228', 'RECNGTUELVJV-412', 'YYDEIFLIBH-138', 'YZNULB-403', 'KTLRGISCGUTO-538', 'FFBGMAXJUO-272', 'REXIAC-400', 'VNWARAYX-547', 'ZBPWPUKPPCHL-395', 'JILRHEPU-461', 'EVANBJZEAHB-136', 'ZCSDTJ-300', 'UJYLLWONOGWX-332', 'ZKJBMNXRETR-547', 'TQEQMMUTUKOH-181', 'HPTGYKEELF-149', 'FOTJQQJ-542', 'QBWVQZH-399', 'QALQHIANB-529', 'BFNQIHZC-421', 'WSHWAHJYDO-281', 'IWLDHVRM-339', 'OREUBZHJWXUB-377', 'SDREFF-555', 'MNIGYNGNWIP-403', 'ERXTCI-474', 'PILLMSA-355', 'VVIASFIPCXAO-113', 'GQBIUGII-293', 'SGMGDKSPT-303', 'JGLPMEQM-282', 'HBKDITUBWUP-204', 'EXHDEUWMS-211', 'MGNRMPUQTU-192', 'YNOSZMBHJIK-109', 'XFJFAF-293', 'SIGIWPLDQVRT-477', 'AFNYAGFM-135', 'NEIQOAX-451', 'BXKFDS-331', 'YXRTOW-106', 'BROKAYVGWJYV-505', 'CXZMZRRLI-261', 'YGQIMXG-402', 'ZLTZJGWDLU-113', 'GMXGWMMG-540', 'YCRMDREDWIST-541', 'TFALNIVHVP-302', 'UDMJXC-317', 'YEWSSLMGHX-544', 'BMBKQVHYKXXN-394', 'GZGAYG-404', 'LXJXVDYR-103', 'NVVFYTQLKAVQ-247', 'XYZBTV-530', 'SWOFSNV-133', 'PALSNHB-226', 'GOIJFO-537', 'MFERILWB-162', 'RAXLZMJVK-351', 'NGXQWPXQJPYU-247', 'LLSTOKIS-131', 'JGGIRWJWO-113']
capsules = ['QVXR-52', 'BJHA-54', 'IWRM-33', 'QANB-52', 'VWEW-38', 'VWEW-24', 'IWRM-30']
import math
class Contenu():
    def __init__(self,infos):
        to_decode=infos.split("-")
        l=len(to_decode[0])
        self.lettres=to_decode[0][0:2]+to_decode[0][l-2:l]
        self.poids=int(to_decode[1])
        self.arrondi=math.floor(int(to_decode[1])/10)
        self.code=self.lettres+"-"+str(self.arrondi)

def createObject():
    tab_o=[]
    for o in objets:
        new_o=Contenu(o)
        tab_o.append(new_o)
    return tab_o

def findObjinC(tab_o):
    poids=0
    for c in capsules:
        for elt in tab_o:
           if c==elt.code:
            poids=poids+(elt.poids)
    print(poids)


tab_o=createObject()
findObjinC(tab_o)
"""