# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:46:15 2024

@author: Saurabh Kumar
"""

class Addition:
    
    
    def __init__(self):
        self.x=10;
        self.y=20;
        
    
    def add(self):
        
        print("print statement", self.x + self.y)  
        
        
        
        z= (self.x + self.y)
        
        return z 
    
        variable =20     # dead statement
        print(variable)  # dead statement
        
        


a=Addition()

temp= a.add()
print(temp)