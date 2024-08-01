# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:09:30 2024

@author: saura
"""



class ZPattern:
    
    def zpattern(self):
        n=11
        for i in range(n):
            
            for j in range(n):
                
                if i==0 or i==n-1 or j==(n-(i+1)):
                    
                    print("*", end=' ')
                else: 
                    
                    print(' ', end=' ')
            
            print()


z=ZPattern()

z.zpattern()
                    