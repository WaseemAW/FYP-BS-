# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:00:21 2021

@author: Muhammad Waseem
"""

import json

password=input("Please Enter Password")

data = {'password':password}

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)