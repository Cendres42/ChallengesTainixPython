orders = ['76,melange,muscade', '65,noir,cannelle', '71,au_lait,piment,chocolat_brule', '67,noir,cannelle', '72,melange,muscade,tasse_froide']
import math
tab_choc=[]

class Chocolat():
    def __init__(self,order):
        args=order.split(",")
        self.temp=int(args[0])
        self._type=args[1]
        self._epice=args[2]
        if len(args)>3:
            self._evnt=args[3]
        else: 
            self._evnt=""
#
# @brief fonction qui détermine variation température selon type de chocolat
#  
    def tempselontype(self):
        if self._type=="noir":
            self.temp+=5
        elif self._type=="au_lait":
            self.temp+=10
        elif self._type=="blanc":
            self.temp+=15
        elif self._type=="melange":
            self.temp+=12
#
# @brief fonction qui détermine variation température selon épice
#  
    def tempselonepices(self):
        if self._epice=="cannelle":
            self.temp+=4
        elif self._epice=="muscade":
            self.temp+=7
        elif self._epice=="piment":
            self.temp+=9
        elif self._epice=="vanille":
            self.temp+=1
#
# @brief fonction qui détermine variation température selon évènement particulier
#      
    def tempselonevnt(self):
        if self._evnt=="tasse_froide":
            self.temp*=2
        elif self._evnt=="epice_surprise":
            self.temp+=10
        elif self._evnt=="chocolat_brule":
            self.temp-=10
        elif self._evnt=="":
            self.temp=self.temp
    
    def prepare(self):
        self.tempselontype()
        self.tempselonepices()
        self.tempselonevnt()

    @property
    def temp(self):
    #température du chocolat dans la tasse
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value
#
# @brief fonction de récupération des données du tableau orders 
# 
def recupDonnees():
    for order in orders:
    #création du tableau d'objets à partir des données
        chocolat=Chocolat(order)
        tab_choc.append(chocolat)

#
# @brief fonction qui prépare les chocolats
# 
def cuisine():
    recupDonnees()
    tempTotale=0
    for choc in tab_choc:
        choc.prepare()
        tempTotale=tempTotale+choc.temp
        print(choc.temp)
    moyenne=math.ceil(tempTotale/len(tab_choc))
    print(moyenne)
    
cuisine()  
    



