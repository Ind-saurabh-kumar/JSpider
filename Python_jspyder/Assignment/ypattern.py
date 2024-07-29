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
                
                
                if j==i or j==(n-i+1):
                    
                    print("*", end=' ')
                else:
                    print(' ', end=' ')
                    
            print()


y=YPattern()
y.yPatt()