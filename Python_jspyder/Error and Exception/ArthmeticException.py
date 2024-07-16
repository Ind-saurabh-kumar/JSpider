# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:11:51 2024

@author: saura
"""

class TestException:
    
    def divideTheNumber(self, a, b):
        
        try:
            c=a/b
            print(c)
            
        except ZeroDivisionError:
            print("Please remove zero from denominator")
        
    
    def display(self):
        print("I am working.....")


t=TestException()
t.divideTheNumber(10, 0)
t.display()
            