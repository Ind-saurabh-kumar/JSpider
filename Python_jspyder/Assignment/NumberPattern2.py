# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:10:37 2024

@author: saura
"""

class NumPrymid:
    
    def numPry(self):
        
        n=10
        
        for i in range(n):
            
            for j in range(n-i+1):
                print(' ', end=' ')
                
            for k in range(2*i+1):
                
            
                if k%2==0:
                    print('1', end=' ')
                
                else:
                    print('0', end=' ')
                 
            
            
            print()
            

np=NumPrymid()
np.numPry()