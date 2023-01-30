# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:03:09 2021

@author: imran
"""

import os, sys
from PIL import Image

inputpath = "C:/Users/imran/OneDrive/Pictures/sw screenshots/"
dirs = os.listdir(inputpath)
outputpath= "C:/Users/imran/OneDrive/Pictures/PY_sw/"


for item in dirs:
    im = Image.open(inputpath+item)
    #print(path, item)
    rgb_im = im.convert('RGB')
    f, e = os.path.splitext(inputpath+item)
    #print(f , e)    
    fname= f.split('/')[-1]
    #print(fname)
    imResize = rgb_im.resize((307,222), Image.ANTIALIAS)
    imResize.save(outputpath+fname+ '.jpg', 'JPEG', quality=84)