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
import json
#import NEW_try
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
        m_title=Label(Manage_frame,text='Encryption Second Stage',bg='#04444a',fg='white' ,font=('time new roman',30,'bold')).place(x=100,y=10,width=1000)
       
        
        Password_Frame=Frame(self.root,bd=4)
        Password_Frame.place(x=520,y=350)
        
        lbl_password=Label(Password_Frame,text='password',bg='#04444a',fg='white',font=('time new roman',12,'bold'))
        lbl_password.grid(pady=0,padx=0,sticky='w')
        
        self.text_password=Entry(Password_Frame,font=('time new roman',14,'bold'),bd=2,relief=GROOVE)
        self.text_password.grid(row=0,column=2,pady=5,padx=5,sticky='w')
        
        
        
        self.pic=ImageTk.PhotoImage(file='12.png')
        self.pic_set=Label(self.root,image=self.pic).place(x=650,y=200,width=150,height=150)
        image = Image.open('12.png')
        
        
        
        #Buttons
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg='#04444a')
        btn_frame.place(x=350,y=530,width=600)
        RGB_btn=Button(btn_frame,text='Click for TSED Encryption',command=self.TSED,width=19).grid(row=0,column=1,padx=90)
        TSED_btn=Button(btn_frame,text='Click for Decryption',command=self.decrypt,width=21).grid(row=0,column=2,padx=15)
        #save_btn=Button(btn_frame,command=self.text_gui2,text='Next',width=12).grid(row=0,column=3,padx=15)
    
    def decrypt(self):
        #self.root.destroy()
        call(["python", "1st_decryption.py"])  
    
    def TSED(self):
        a=self.text_password.get()
        data={'password':a}
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
        #messagebox.showinfo('Info','Please remmeber your password')
        img=plt.imread(r"12.png")
        img= (img*255).round().astype(np.uint8)
        rows=img.shape[0]
        col=img.shape[1]
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
        cv2.imwrite('Second.png',img)
        #img.save(r'Second_Encrypion.png')
        #img2 = img1
        self.pic=ImageTk.PhotoImage(file='Second.png')
        self.pic_set=Label(self.root,image=self.pic).place(x=650,y=430,width=130,height=130)
        new_img=img1.resize((400,400))
        image = Image.open('Second.png')
   
        

root =tk.Tk()
obj = Window(root)
root.mainloop()
