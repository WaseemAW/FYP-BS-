# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:54:53 2021

@author: Muhammad Waseem
"""
from subprocess import call
import tkinter as tk
from tkinter import*
import os
from tkinter import filedialog
from PIL import Image,ImageTk,ImageDraw
import matplotlib.pyplot as plt,numpy as np,random




    
class Window: 
    output_image_size=0
    def __init__(self,root):
        self.root=root
        self.root.title('Image Encryption and Decryption')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#08A3D2')
       
        title=Label(self.root,text="Image Encryption and Decryption",relief=GROOVE,font=('time new roman',40,'bold'),bg='#04444a',fg='white')
        title.pack(side=TOP,fill=X)
      
        #FRAME
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Manage_frame.place(x=40,y=100,width=640,height=580)
        m_title=Label(Manage_frame,text='Encryption',bg='#04444a',fg='white' ,font=('time new roman',30,'bold')).place(x=20,y=10,width=590)
      
        #Button
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg='#04444a')
        btn_frame.place(x=10,y=530,width=600)
        
        browsbtn=Button(btn_frame,command =self.brw_enc_img,text='Browse Image',width=10).grid(row=0,column=0,padx=10)
      
        
        
        Enc_btn=Button(btn_frame,command =self.Encryption,text='Click for Encryption',width=20).grid(row=0,column=1,padx=80)
        save_btn=Button(btn_frame,text='Save',width=10).grid(row=0,column=3,padx=50)

        #Frame 2
        Manage2=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Manage2.place(x=690,y=100,width=640,height=580)
        m_title=Label(Manage2,text='Decryption',bg='#04444a',fg='white' ,font=('time new roman',30,'bold')).place(x=20,y=10,width=590)
        btn_frame=Frame(Manage2,bd=4,relief=RIDGE,bg='#04444a')
        btn_frame.place(x=10,y=530,width=600)
        
        browsbtn=Button(btn_frame,command =self.brw_dec_img,text='Browse decrypted Image',width=20).grid(row=0,column=0,padx=10)
        dec_btn=Button(btn_frame,text='click here for decryption',width=20).grid(row=0,column=1,padx=80)
        dec_save_btn=Button(btn_frame,text='Save',width=10).grid(row=0,column=2,padx=20)
    #=====Encryption    
    def brw_enc_img(self):
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
                panel.place(x=100,y=250,width=200,height=200)
                
    def Encryption(self):
        
        key=[]
        while len(key)!=256:
            j=random.randrange(0,256)
        if j not in key:
           key.append(j)
           print(j)

        def decrypt_image(myfile,key, rows, col):
            img1=np.zeros((rows,col,3),dtype=int)
            for i in range(rows):
                for j in range(col):
                    for k in range(3):
                        img1[i][j][k]=key.index(myfile[i][j][k])
            return img1

        img3=decrypt_image(img1,key,rows,col)
        imshow(img3)

      # panel = Label(self.root, image=img3)
     #  panel.image = img3
      # self.output_image_size = os.stat(img3)
      # self.o_image_w, self.o_image_h = myimg.size
       #panel.place(x=200,y=250,width=200,height=200)

   
    
   

   #Decryption
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
                panel.place(x=750,y=250,width=200,height=200)


root =tk.Tk()
obj = Window(root)
root.mainloop()

