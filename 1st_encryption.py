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
        m_title=Label(Manage_frame,text='Encryption First Stage',bg='#04444a',fg='white' ,font=('time new roman',30,'bold')).place(x=100,y=10,width=1000)
        
        lbl_text=Label(Manage_frame,text='Plain Text',fg='black',font=('time new roman',10,'bold'))
        lbl_text.grid(row=7,column=0,pady=100,padx=350,sticky='w')
       
        self.text=Text(Manage_frame,width=75,height=10,font=('',10))
        self.text.grid(padx=350,pady=0,sticky='w')
        self.text.place(x=350,y=130)
        
       
        
        
        
        
        #Buttons
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg='#04444a')
        btn_frame.place(x=350,y=530,width=600)
        RGB_btn=Button(btn_frame,command=self.First_Encrypt,text='Click for First Encryption',width=19).grid(row=0,column=1,padx=90)
        TSED_btn=Button(btn_frame,command=self.Second_Encrypt,text='Click for Second Encryption',width=21).grid(row=0,column=2,padx=15)
        #save_btn=Button(btn_frame,command=self.text_gui2,text='Next',width=12).grid(row=0,column=3,padx=15)

#FUNCTION
    def Second_Encrypt(self):
        self.root.destroy()
        call(["python", "2nd_encryption.py"])    


        
    def First_Encrypt(self):
        data = self.text.get('1.0',END)
        tokens = word_tokenize(data)
        maxValue = max(tokens, key=lambda x: len(x))
        count = 0
        for i in maxValue:
             count = count +1   
        asc = []
        for c2 in data:
            asc.append(ord(c2))
            asc1 = np.array(asc)                 
            r1 = count
            c1 = len(tokens)
            rgbArray = np.zeros((1,len(asc1),3), 'uint8')
            for r in range(0,1):
                for c, i in zip(range(0, len(asc1)), asc1):
                    rgbArray[r,c,0] = i
                    rgbArray[r,c, 1] = np.random.randint([0],i)
                    rgbArray[r,c, 2] = np.random.randint(i,[200])
                    img = Image.fromarray(rgbArray)
                   # print(img)
            img.save(r'First.png')
            
            self.pic=ImageTk.PhotoImage(file='First.png')
            self.pic_set=Label(self.root,image=self.pic).place(x=650,y=430,width=130,height=130)
            image = Image.open('First.png')
    
    img = (np.random.standard_normal([90, 90, 3]) * 255).astype(np.uint8)
    cv2.imwrite('12.png',img)
    

  
           
   
root =tk.Tk()
obj = Window(root)
root.mainloop()