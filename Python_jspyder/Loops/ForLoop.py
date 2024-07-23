# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:56:32 2024

@author: saura
"""


class ForLoop:
    
    def forintLp(self):
        
        a=[1,2,3,4,5,6]

        for i in a:
            print(a[i-1])
            
    def forstrLp(self):
        
        name="Saurabh Kumar"
        
        for n in name:
            print(n)
            
    def forRangeLp(self):
        
        for j in range(1, 10, 2):
            print(j)
            
            

f=ForLoop()
f.forintLp()

f.forstrLp()
f.forRangeLp()