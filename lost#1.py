nombres = [4, 8, 15, 16, 23, 42]
codes = ['1 2 - 3 3 + 6', '5 2 4 - 2 1 6 - 1', '3 1 5 5 + 1 2']# NE PAS TOUCHER
class Decodage():
    def __init__(self,code):
        self._code=list(code.replace(" ",""))
        self._decoded=[]
    
    def __repr__(self):
        return self._code
    
    def useTheKey(self,nb):
        for j in range(len(self._code)):
            if self._code[j].isdigit()==True:
                v = int(self._code[j])
                x = nb[v-1]
                self._code[j]=x

    def prioritaires(self):
        new_tab=[]
        for j in range(len(self._code)):
            if self._code[j-1]=="-" or self._code[j]=="-"or self._code[j]=="+" or self._code[j-1]=="+":
                continue
            elif j==len(self._code)-1:
                value=self._code[j]
                new_tab.append(value)
                continue
            elif str(self._code[j+1]).isdigit()==True:
                value=self._code[j]
                new_tab.append(value)
            elif self._code[j+1]=="-":
                value=int(self._code[j])-int(self._code[j+2])
                new_tab.append(value)
            elif self._code[j+1]=="+":
                value=int(self._code[j])+int(self._code[j+2])
                new_tab.append(value)
        self._decoded=new_tab

    def multipla(self):
        value=1
        for j in range(len(self._decoded)):
            value=value*self._decoded[j]
        #print( value)
        return value

tab_obj=[]

for code in codes:
    boutDeCode=Decodage(code)
    tab_obj.append(boutDeCode)
 
total=0
for obj in tab_obj:
    obj.useTheKey(nombres)
    obj.prioritaires()
    total=total+obj.multipla()
print(total)
