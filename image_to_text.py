# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:31:28 2021

@author: Muhammad Waseem
"""

from PIL import Image
import numpy as np
from random import randint
from nltk.tokenize import word_tokenize
def fun():
    #f= open('doc.txt','r')
    data = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. '
    #data = Image.open('new.png')
   # print(data)
    tokens = word_tokenize(data)
    #print(tokens)
    maxValue = max(tokens, key=lambda x: len(x))
    count = 0
    for i in maxValue:
        count = count +1   
    asc = []
    for c2 in data:
        asc.append(ord(c2))
     #print(asc)
    asc1 = np.array(asc)
    #print
    #asc.remove(32)
    r1 = count
    #print(r1)
    c1 = len(tokens)
    #print(c1)
    
    
    rgbArray = np.zeros((1,len(asc1),3), 'uint8')
    for r in range(0,1):
         for c, i in zip(range(0, len(asc1)), asc1):
              #print(i)
              rgbArray[r,c,0] = i
              rgbArray[r,c, 1] = np.random.randint([0],i)
             # print(rgbArray[r,c, 1])
              rgbArray[r,c, 2] = np.random.randint(i,[200])
    
              img = Image.fromarray(rgbArray)
    img.save(r'mam.png')
    img.show()

if __name__ == '__main__':
    fun()



        
        
        