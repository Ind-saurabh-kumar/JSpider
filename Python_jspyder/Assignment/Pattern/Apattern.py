# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:45:45 2024

@author: saura
"""

class APattern:
    
    def pattA(self):
        
        n=9
        
        for i in range(n):
            
            for j in range(n):
                
                if i==0 or i==round(n/2) or j==0 or j==n-1:
                    
                    print("*", end=' ')
                
                
                else:
                    
                    print(' ', end=' ')
                    
            print()
            


aPatt=APattern()
aPatt.pattA()