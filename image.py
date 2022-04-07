# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:34:45 2021

@author: Muhammad Waseem
"""
import tkinter as tk
from tkinter import*
import os
from tkinter import filedialog
from PIL import Image,ImageTk,ImageDraw
def image(self):
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
                panel.place(x=620,y=300,width=300,height=200)