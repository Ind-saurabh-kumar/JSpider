# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:51:06 2024

@author: saura
"""



class SquarePatt:
    
    def patternSq(self):
    
        for i in range(5):
        
            for j in range(5):
                
                #print(f"{i},{j} ", end='')
                
                
                print("* ", end='')
            
            print()
            
    
    def patternA(self):
        
        n=5
        
        for i in range(n):
            
            for j in range(n):
                
                
                if i==0 or i==n-1 or j==0 or j==n-1:
                    print("*",end=' ')
            
            
                else:
                    print(' ', end=' ')
            
            print()
                    
                    
            
                
                


s=SquarePatt()
#s.patternSq()

s.patternA()