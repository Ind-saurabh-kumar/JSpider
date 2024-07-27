# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:55:04 2024

@author: saura
"""



m=[[1,2,3],[4,5,6],[7,8,9]]


for i in range(len(m)):
    print(m[i])


for i in range(len(m)):
    
    for j in range(len(m[i])):
        
        print(f"{m[i][j]}",end=',')
    print()