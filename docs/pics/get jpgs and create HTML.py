#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:42:06 2020

@author: caramelo
"""

from os import listdir
from os import remove

folders = listdir()
try:
    remove("HTML raw")
except:
    1

html = open("HTML raw", "w+")

numbs = 0
for folder in folders:
    print(folder)
    try:
        a = listdir(folder) 
        html.write( '<div ' )
        html.write( 'id="' )
        html.write( folder[:3] )
        html.write( '" style="background-color: #E2768A">' )                    
        html.write( '<h1 style="text-align:center;color:white;">')
        html.write( folder )
        html.write( '</h1> </div> ' )
                
        for i in a:
            if i[-3:] == "jpg":
                html.write( '<img src="pics/' )
                html.write( folder )
                html.write( '/' )
                html.write( i )
                html.write( '" loading="lazy" style=" width:300px ; padding:10px;" > ' )
                html.write( '\n' )
                numbs=numbs+1
                print(numbs)
    except:
        print("not")
    
    
    
html.close()
print(numbs)
    
