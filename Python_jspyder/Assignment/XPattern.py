# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:21:15 2024

@author: saura
"""

class XPattern:
    
    def xPatt(self):
        
        n=10
        
        for i in range(n):
            
            for j in range(n):
                
                if j==i or  j==(n-(i+1)) or i==j:
                    
                    print("*", end=' ')
                else:
                    
                    print(' ', end=' ')
            
            print()
            



x=XPattern()
x.xPatt()