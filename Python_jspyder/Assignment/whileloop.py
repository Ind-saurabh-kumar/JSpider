# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:41:47 2024

@author: saura
"""


listData=[23,4,83,8,94,28,39,89,24]

class Assign2:
    
    
    
    def oddFun(self):
        
         i=0
         while i<len(listData):
             
             if listData[i]%2!=0:
                 print(listData[i])
                 
             i=i+1
             
             
             
    def evenFun(self):
        
         i=0
         while i<len(listData):
             
             if listData[i]%2==0:
                 print(listData[i])
                 
             i=i+1



a2=Assign2()

a2.oddFun()

a2.evenFun()
        
        