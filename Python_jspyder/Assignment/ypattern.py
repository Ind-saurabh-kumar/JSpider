# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:21:28 2024

@author: saura
"""

class YPattern:
    def yPatt(self):
        
        n=9
        
        for i in range(n):
            
            for j in range(n):
                
                if (i==0 or j==n-1):
                    print('*', end=' ')
                
                
            print()
        
        
        

y = YPattern()
y.yPatt()