# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:21:29 2024

@author: saura
"""




class PiramidPattern:
    
    def pattPiramid(self):
        
        n=10
        
        for i in range(n):
            
            for j in range(n-i+1):
                
                print(' ', end=' ')
            
            
            for k in range(2*i+1):
                
                print("*", end=' ')
            
            print()
            

p=PiramidPattern()
p.pattPiramid()