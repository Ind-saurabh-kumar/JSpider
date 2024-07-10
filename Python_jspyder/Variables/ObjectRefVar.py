# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:36:53 2024

@author: Saurabh Kumar
"""

class ObjectRefVar:
    price =300000  # --> Class variable

    def __init__(self):
        print("address from self", self)
        
        self.color ="red" # --> Instace variable 
        
        print(self.color)
        
        print(ObjectRefVar.price)
    
        
x=ObjectRefVar()  # --> Object reference variable, trigger the init constructor for object creation

print("address from x", x)

print(x.color)
        