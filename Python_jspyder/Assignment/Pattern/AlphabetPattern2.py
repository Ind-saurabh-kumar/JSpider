# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:34:28 2024

@author: saura
"""



class CharPrymid:
    
    def charPry(self):
        
        n=10
        
        for i in range(n):
            
            for j in range(n-i+1):
                print(' ', end=' ')
                
            for k in range(2*i+1):
                
                if k==j:
                    print('*', end=' ')
                else:
                    print(chr(65+k), end=' ')
            
            print()
            

cp=CharPrymid()
cp.charPry()