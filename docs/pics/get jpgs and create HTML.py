#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:42:06 2020

@author: caramelo
"""

from os import listdir
from os import remove

a = listdir()
try:
    remove("HTML raw")
except:
    1

html = open("HTML raw", "w+")

for i in a:
    if i[-3:] == "jpg":
        html.write( '<img src="pics/'  )        
        html.write( i )
        html.write( ' " style=" width:250px ;" > ' )
        html.write( '\n' )
    
