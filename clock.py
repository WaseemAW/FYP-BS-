# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:18:05 2021

@author: Muhammad Waseem
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:01:20 2021

@author: Muhammad Waseem
"""
import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
class Wellcome_Window:  
    def __init__(self,root):
        self.root=root
        self.root.title('CLOCK')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#021e2f')
        
        #title=Label(self.root,text="Welcome to Black Box",font=('time new roman',50,'bold'),bg='#04444a',fg='white').place(x=0,y=5,relwidth=1)
        
        
        #BACKGROUND
        left_lbl=Label(self.root,bg='#08A3D2',bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        
        right_lbl=Label(self.root,bg='#031F3C',bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        #FRAME
        login_frame=Frame(self.root,bg='white')
        login_frame.place(x=250,y=100,width=800,height=500)
        
        
        self.lbl=Label(self.root,bg='#081923',bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()
        
       
       #self.clock_image()
   
        
        
    def clock_image(self,hr,min_,sec_):
        clock = Image.new('RGB',(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        
        bg=Image.open('6.jpg')
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill='#DF005E',width=4)
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill='green',width=3)
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill='yellow',width=2)
        draw.ellipse((195,195,210,210),fill='black')
        clock.save('clock_new.jpg')
        
    
        
    def working(self):
        h= datetime.now().time().hour 
        m= datetime.now().time().minute
        s= datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
       #print (h,m,s)
       # print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        #self.img=Image.open('clock_new.png')
        self.img=ImageTk.PhotoImage(file='clock_new.jpg')
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
        
        
        
root =tk.Tk()
obj = Wellcome_Window(root)
root.mainloop()