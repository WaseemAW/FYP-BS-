# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:23:43 2021

@author: Muhammad Waseem
"""
import matplotlib.pyplot as plt,numpy as np,random
from numpy import zeros


#Enter the address of the image inside r""
#Enter a jpg image.
img=plt.imread(r"mam.png")
img= (img*255).round().astype(np.uint8)

rows=img.shape[0]
col=img.shape[1]

plt.title("First Encryption Image")

plt.imshow(img)
plt.show()
key=[]
while len(key)!=256:
    j=random.randrange(0,256)
    if j not in key:
        key.append(j)
    
        

def encrypt_image(img, key, rows, col):
    img1=np.zeros((rows,col,3),dtype=int)
    for i in range(rows):
        for j in range(col):
            for k in range(3):
                img1[i][j][k]=key[img[i][j][k]]
    return img1

img1=encrypt_image(img,key,rows,col)

plt.title(" 2nd Encrypted Image")
plt.imshow(img1)
plt.show()

def decrypt_image(img,key, rows, col):
    img1=np.zeros((rows,col,3),dtype=int)
    for i in range(rows):
        for j in range(col):
            for k in range(3):
                img1[i][j][k]=key.index(img[i][j][k])
    return img1

img1=decrypt_image(img,key,rows,col)
print(img1)
plt.title(" 1st decrypted Image")
plt.imshow(img1)
plt.show()


img3=decrypt_image(img1,key,rows,col)
res= []
li =[]
p = []
li1 = []
for i in img3[:,:,0]:
    
    res.extend(chr(num) for num in i) 
    
str1=""

plt.title("Decrypted Image")
plt.imshow(img3)
plt.show()

print("\n\n\nConvert decrypted image into text form: \n\n\n", str1.join(res))
