# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:58:56 2024

@author: Saurabh Kumar
"""

class ClassVariable:
    
    price=300000  # --> Class Variable
    
    def __init__(self):
        print(self)
        self.color="red" # --> Instance Variable
        print(self.color) 
        
        print(ClassVariable.price)
        





print(ClassVariable.price)

