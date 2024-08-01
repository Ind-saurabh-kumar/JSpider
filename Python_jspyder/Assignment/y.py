# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:21:28 2024

@author: saura
"""


class YPattern:
    
    def yPatt(self):
        
        n=int(input("Enter the lenght of y:\n"))
        
        for i in range(n):
            
            for j in range(n):
                
                
                if ((i==j or i==(n-j)-1 )and i<=n//2-1) or ((i>=n//2 and j==n//2) and i>=n//2) :
                    
                    print("*", end=' ')
                else:
                    print(' ', end=' ')
            print()


y=YPattern()
y.yPatt()