import sys
import os
import pandas as pd
import numpy as np
#import matplotlib 
import matplotlib.pyplot as plt
data="""Mobiles get set for visual radio  The growth in the {{infobox my name is sam.
i am her to show my jalwa....... how are you?
}} hello everyone"""
def findAndRemoveInfoBox(data):
     #infoBox=[]
    s= "{{infobox"
    n = len(data)
    l= len(s)
    for position in range(0,n):
        ss = data[position:position+l]
        if ss == s:
            for subposition in range(position+l,n):
                if data[subposition:subposition+2]== "}}":
                       beforeslice = data[0:position]
                       afterslice = data[subposition+2:]
                       d = beforeslice+afterslice
                       return d
    return data
            
a = findAndRemoveInfoBox(data)
print(a)