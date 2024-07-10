# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:24:20 2024

@author: saura
"""

class Test:
    
    def testMethod(self, x):
        
        if x>15:
            print("x is valid")
            
        print("x is invalid") 
    
    
    
    
    
t=Test()
t.testMethod(20)

print("****Lower Value passed***")

t.testMethod(10)

