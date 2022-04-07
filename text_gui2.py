# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:47:57 2021

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




    
class Window:  
    def __init__(self,root):
        self.root=root
        self.root.title('Text Encryption and Decryption')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#08A3D2')
        title=Label(self.root,text="Text Encryption and Decryption",relief=GROOVE,font=('time new roman',40,'bold'),bg='#04444a',fg='white')
        title.pack(side=TOP,fill=X)
        #Frame 2
        Manage2=Frame(self.root,bd=4,relief=RIDGE)
        Manage2.place(x=90,y=100,width=1180,height=580)
        m_title=Label(Manage2,text='Decryption',bg='#04444a',fg='white' ,font=('time new roman',30,'bold')).place(x=100,y=10,width=1000)
        btn_frame=Frame(Manage2,bd=4,relief=RIDGE,bg='#04444a')
        btn_frame.place(x=250,y=530,width=600)
        key_lbl=Label(Manage2,text='Key',fg='black',font=('time new roman',10,'bold'),width=15,height=4).place(x=220,y=270,width=70)
        key_conf=Text(Manage2,width=15,height=4).place(x=300,y=290,width=530,height=30)
        
        text_enc_lbl=Label(Manage2,text='Plain Text',fg='black',font=('time new roman',10,'bold'),width=15,height=4).place(x=210,y=315,width=70)
        text_enc_lbl_conf=Text(Manage2,width=15,height=4).place(x=300,y=330,width=530,height=190)

        browsbtn=Button(btn_frame,command=self.brw_dec_img,text='Browse decrypted Text',width=20).grid(row=0,column=0,padx=10)
        dec_btn=Button(btn_frame,text='click here for decryption',width=20).grid(row=0,column=1,padx=80)
        dec_save_btn=Button(btn_frame,text='Save',width=10).grid(row=0,column=2,padx=20)

      #======= Browse Decryption image
    def brw_dec_img(self):
           myfile = filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
           if not myfile:
              messagebox.showerror("Error","You have selected nothing !")
           else:
                myimg = Image.open(myfile, 'r')
                myimage = myimg.resize((300, 200))
                img = ImageTk.PhotoImage(myimage)
                panel = Label(self.root, image=img)
                panel.image = img
                self.output_image_size = os.stat(myfile)
                self.o_image_w, self.o_image_h = myimg.size
                panel.place(x=920,y=180,width=200,height=200)
                
    def enc_RGB(self):
      data = self.text_conf
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
      rgbArray = np.zeros((1,c1,3), 'uint8')
      for r in range(0,1):
         for c, i in zip(range(0, c1), asc1):
              rgbArray[r,c,0] = i
              rgbArray[r,c, 1] = np.random.randint(i,200)
              rgbArray[r,c, 2] = np.random.randint(0, i)
      img = Image.fromarray(rgbArray)
      print(rgbArray)
      img.show()
root =tk.Tk()
obj = Window(root)
root.mainloop()