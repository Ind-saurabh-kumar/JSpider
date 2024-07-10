# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:01:16 2024

@author: Saurabh Kumar
"""

class InstanceVariable:
    
    def __init__(self):  # --> Default Constructor, implicit parameter
        print(self)
        
        self.color = "red"   # --> instance variable
        print(self.color)

InstanceVariable();