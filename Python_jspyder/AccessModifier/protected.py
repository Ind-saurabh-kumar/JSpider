# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:55:52 2024

@author: Saurabh Kumar
"""

class Father:
    
    _abc = 100 
    
    def _smoke(self):
        print("Smoking")
        
        
f=Father()
f._smoke()
f._abc


class Son(Father):
    pass 



s=Son()
s._smoke()
s._abc
     