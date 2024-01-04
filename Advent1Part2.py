
import os
import math   

def recupNombres():
    file = open('C:/Users/Gwen/Desktop/Data/JeuxPython/advent1.txt', "r")
    # utiliser readlines pour lire toutes les lignes du fichier
    line = file.readline()
    nbConcat=0
    # La variable "lignes" est une liste contenant toutes les lignes du fichier
    dico={"zero":"0","one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9","0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
    while line:
        positionI=9999
        valeurI=""
        positionF=-1
        valeurF=""
        for elt in dico:
            if elt in line:
                tmp=line.find(elt)
                if tmp<positionI:
                    positionI=tmp
                    valeurI=elt
                tmp=line.rfind(elt)
                if tmp>positionF:
                    positionF=tmp
                    valeurF=elt
        nbConcat=nbConcat+int(dico[valeurI]+dico[valeurF])
        line = file.readline()
    print(nbConcat)

recupNombres()