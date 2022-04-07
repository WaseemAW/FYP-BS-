# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:12:42 2021

@author: Muhammad Waseem
"""

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile



root= tk.Tk()
canvas=tk.Canvas(root, width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)

#logo
logo = Image.open('D:\logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image= logo
logo_label.grid(column=1,row=0,padx=0,pady=0)



#instruction
name=tk.Label(root, text="University of Baltistan, Skardu",font=('time new roman',25,'bold'),bg='white',fg='Blue').place(x=250,y=150)
instructions = tk.Label(root,text="Image Splicing",font=('time new roman',25,'bold'),bg='white',fg='Blue').place(x=340,y=200)
#btn_img = tk.Label(root,text='START ',command = '',font=('time new roman',20,'bold'),fg='white',bg='#081923').place(x=390,y=550)

#Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_text, command='', font="Raleway",bg="#20bebe",fg="white", height=2,width=15)
browse_text.set("Start")
browse_btn.grid(column=1,row=3)
canvas=tk.Canvas(root, width=900,height=250)
canvas.grid(columnspan=3)

root.mainloop()
