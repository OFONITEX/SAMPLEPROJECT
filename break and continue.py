# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 06:03:21 2021

@author: HP
"""

# print a table for first 10 numbers 

for i in range (1,20,1):
    
    if i > 10:
        break
    
    for j in range (1,11,1):
        result = i * j
        
        print(result, end=" ")
    print("")