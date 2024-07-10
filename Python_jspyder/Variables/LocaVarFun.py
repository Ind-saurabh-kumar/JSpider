# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:45:45 2024

@author: Saurabh Kumar
"""

class LocalVarFun:
    
    price =300000
    
    def __init__(self):    #--> implicit local variable "self"
        
        a=10;   # --> Local variable of a method
        print(a)
        
        print("address from self", self)
        
        self.color="red"  # --> instance variable
        print(self.color)
        
        print(LocalVarFun.price)
        
        


x = LocalVarFun();
print("address from x ", x)

print(x.color)

print(x.price)