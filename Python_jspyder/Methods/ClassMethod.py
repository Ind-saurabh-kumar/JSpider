# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:25:25 2024

@author: Saurabh Kumar
"""

class ClassMethod:
    
    def __init__(self):  # --> Default Constructor
        None;
    
    def teachers(self):   # --> Instance Method
        print("Teacher is teaching")
        
    
    @classmethod    #--> decorator
    def evaluate(cls):  #--> class method
        print("Teacher Evaluate")
        
        
        
ClassMethod.evaluate()    # --> classmethod Invoked

c=ClassMethod()      # --> object cration
c.teachers()          # --> fuction invoked