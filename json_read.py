# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:02:35 2021

@author: Muhammad Waseem
"""

import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    if(data['password'] == input("Please Enter Password")):
        print("you have access")
    else:
        print ("sorry wrong password")