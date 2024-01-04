import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
import seaborn as sns
import scipy.stats as st
    
def recupNombres2():
    file = open('C:/Users/Gwen/Desktop/Data/JeuxPython/advent1.txt', "r")
    # utiliser readlines pour lire toutes les lignes du fichier
    # La variable "lignes" est une liste contenant toutes les lignes du fichier
    line = file.readline()
    # Itérer sur les lignes
    R=0
    vi=""
    vf=""
    while line:
        i=0
        for i in line:
            test=i
            if test.isdigit()==True :
                if vi=="" :
                    vi=test                    
                vf=test
                      
            # utilisez readline() pour lire la ligne suivante
            #print (len(line))
               
        print(vi+vf)
        R=R+int(vi+vf)
        vi=""
        line = file.readline()

    print( R)
    file.close()

recupNombres2()