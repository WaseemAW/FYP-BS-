# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:33:48 2021

@author: Muhammad Waseem
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = (np.random.standard_normal([90, 90, 3]) * 255).astype(np.uint8)
cv2.imwrite('12.png',img)