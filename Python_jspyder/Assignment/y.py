# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:21:28 2024

@author: saura
"""


class YPattern:
    
    def yPatt(self):
        
        n=10
        
        for i in range(n):
            
            for j in range(n):
                
                
                if (j==i or j==(n-i+1)  or i<(n//2)  or j<(n//2)):
                    
                    print("*", end=' ')
                else:
                    print(' ', end=' ')


y=YPattern()
y.yPatt()