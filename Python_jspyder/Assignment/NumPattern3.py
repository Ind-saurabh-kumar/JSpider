# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:50:52 2024

@author: saura
"""

class NumPrymid:
    
    def numPry(self):
        
        n=10
        
        for i in range(n):
            
            for j in range(n-i+1):
                print(' ', end=' ')
                
            for k in range(2*i+1):
                
            
                if i%2==0:
                    print('*', end=' ')
                
                    
                 
            
            
            print()
            

np=NumPrymid()
np.numPry()