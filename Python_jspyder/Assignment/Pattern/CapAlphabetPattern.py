# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:53:26 2024

@author: saura
"""

class CapAlphPrymid:
    
    def numPry(self):
        
        n=10
        
        for i in range(n):
            
            for j in range(n-i):
                print(' ', end=' ')
                
            for k in range(2*i+1):
                
                if k==0 or k==(i*2):
                    print('*', end=' ')
                    
                else:
                    print(chr(65+k-1), end=' ')
                
            
            print()
            

np=CapAlphPrymid()
np.numPry()