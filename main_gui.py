# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:01:20 2021

@author: Muhammad Waseem
"""
from subprocess import call
import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk,ImageDraw


    
class Wellcome_Window:  
    def __init__(self,root):
        self.root=root
        self.root.title('WELCOME')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#08A3D2')
       # title=Label(self.root,text="Welcome to Black Box",font=('time new roman',50,'bold'),bg='#04444a',fg='white').place(x=0,y=5,relwidth=1)
        #BACKGROUND
        #FRAME
        main_frame=Frame(self.root,bg='white')
        main_frame.place(x=250,y=100,width=900,height=500)
        
        title=Label(main_frame,text='UNIVERSITY OF BALTISTAN,SKARDU',font=('time new roman',25,'bold'),bg='white',fg='green').place(x=250,y=50)
        
        project=Label(main_frame,text='(Two Step Encryption,Decryption)',font=('time new roman',20,'bold'),bg='white',fg='gray').place(x=270,y=150)
        
        
        btn_img=Button(main_frame,text='START (TSED)',command = self.Text,font=('time new roman',20,'bold'),fg='white',bg='#081923').place(x=200,y=350,width=650)
        
        self.lbl=Label(self.root,text='\nWELCOME',font=('Book Antiqua',25,'bold'),compound=BOTTOM,fg='white',bg='#081923',bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.logo_set()
        
    
    def Text(self):
        #self.root.destroy()
        call(["python", "1st_encryption.py"])
      
    def logo(self):
        logo = Image.new('RGB',(400,400),(8,25,35))
        draw=ImageDraw.Draw(logo)
        bg=Image.open('logo.png')
        bg=bg.resize((300,300),Image.ANTIALIAS)
        logo.paste(bg,(50,50))
        draw.ellipse((195,195,210,210))
        logo.save('logo_new.png')
      
    def logo_set(self):
         self.img=ImageTk.PhotoImage(file='logo_new.png')
         self.lbl.config(image=self.img)
         self.lbl.after(200,self.logo)

root =tk.Tk()
obj = Wellcome_Window(root)
root.mainloop()