# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:40:10 2024

@author: Saurabh Kumar
"""


class Calculate:
    
    def add(self):  
        x=10
        y=20
        z=x+y
        return z
    
    @classmethod
    def add(cls):
        x=10
        y=20
        z=x+y
        print(z)
        
    @staticmethod
    def add(b,a): 
        x=a
        y=b
        z=x+y
        return z
        

c=Calculate()
c.add(20, 7)
