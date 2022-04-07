# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:27:16 2021

@author: Muhammad Waseem
"""
from PIL import Image,ImageTk,ImageDraw
import tkinter as tk
from tkinter import *
pic=ImageTk.PhotoImage(file='First_Encryption.png')
pic_set=Label(self.root,image=self.img).place(x=650,y=430,width=130,height=130)
image = Image.open('First_Encryption.png')
image=img.resize((400,400))
new_img.save('First_Encryption.png')