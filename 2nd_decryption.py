# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:32:46 2021

@author: Muhammad Waseem
"""
from subprocess import call
import tkinter as tk
from tkinter import*
import os
from tkinter import filedialog
from PIL import Image,ImageTk,ImageDraw
from nltk.tokenize import word_tokenize
from random import randint
import numpy as np
import matplotlib.pyplot as plt,numpy as np,random
import cv2

class Window:  
    def __init__(self,root):
        self.root=root
        self.root.title('Text Encryption and Decryption')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#08A3D2')
        title=Label(self.root,text="Text Encryption and Decryption",relief=GROOVE,font=('time new roman',40,'bold'),bg='#04444a',fg='white')
        title.pack(side=TOP,fill=X)
      
        #FRAME
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_frame.place(x=90,y=100,width=1180,height=580)
        m_title=Label(Manage_frame,text='Decryption Final Stage',bg='#04444a',fg='white' ,font=('time new roman',30,'bold')).place(x=100,y=10,width=1000)
        
        lbl_text=Label(Manage_frame,text='Orignal Text',fg='black',font=('time new roman',10,'bold'))
        lbl_text.grid(row=7,column=0,pady=300,padx=350,sticky='w')
       
        self.text=Text(Manage_frame,width=75,height=10,font=('',10))
        self.text.grid(padx=350,pady=0,sticky='w')
        self.text.place(x=350,y=330)
        
        self.pic=ImageTk.PhotoImage(file='First.png')
        self.pic_set=Label(self.root,image=self.pic).place(x=650,y=200,width=150,height=150)
        image = Image.open('First.png')
       
        
        
        
        
        #Buttons
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg='#04444a')
        btn_frame.place(x=350,y=530,width=600)
    
        RGB_btn=Button(btn_frame,text='Click for TSED Decryption',command=self.decrypt_image1,width=19).grid(row=0,column=1,padx=90)
        TSED_btn=Button(btn_frame,text='Exit Program',command=self.Exit,width=21).grid(row=0,column=2,padx=15)
#FUNCTION
    def Exit(self):
        self.root.destroy()
   
    def decrypt_image1(self):
        img=plt.imread(r"First.png")
        img= (img*255).round().astype(np.uint8)
        rows=img.shape[0]
        col=img.shape[1]
        key=[]
        while len(key)!=256:
            j=random.randrange(0,256)
            if j not in key: 
               key.append(j)   
        def encrypt_image(img,key, rows, col):
             img1=np.zeros((rows,col,3),dtype=int)
             for i in range(rows):
                 for j in range(col):
                     for k in range(3):
                         img1[i][j][k]=key[img[i][j][k]]
             return img1
        img1=encrypt_image(img,key,rows,col)
        def decrypt_image(img,key, rows, col):
            img1=np.zeros((rows,col,3),dtype=int)
            for i in range(rows):
                for j in range(col):
                    for k in range(3):
                        img[i][j][k]=key.index(img[i][j][k])
            return img
        img3=decrypt_image(img1,key,rows,col)
        res= [] 
        for i in img3[:,:,0]:
            res.extend(chr(num) for num in i) 
        str1=""
        txt = str1.join(res)
        self.text.insert(tk.END, txt)
        
            

 
root =tk.Tk()
obj = Window(root)
root.mainloop()

