# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:03:40 2024

@author: Saurabh Kumar
"""

class MethodChain:
    
    def teach(self):
        print("Teacher is teacing.")
        
    
    
    def display(self):
        print("Displaying.....>>>>>>")
        
        self.teach()   #--> method chaining
        


m=MethodChain()
m.display()