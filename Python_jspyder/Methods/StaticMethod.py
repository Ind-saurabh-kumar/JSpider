# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:49:39 2024

@author: Saurabh Kumar
"""


class StaicMethod:
    
    def __init__(self):  # --> Default Constructor
        None;
    
    def teachers(self):   # --> Instance Method
        print("Teacher is teaching")
        
        
    
        
    
    @classmethod    #--> decorator
    def evaluate(cls):  #--> class method    **** cls --> implicit parameter
        print("Teacher Evaluate")
        
    @staticmethod   #--> decorator
    def staicMethods():    # --> Static Method
        print("Teacher is Singing")
        
        
        
StaicMethod.evaluate()    # --> classmethod Invoked

c=StaicMethod()      # --> object cration
c.teachers()          # --> fuction invoked



c.staicMethods()   # --> Static method invoked using object

StaicMethod.staicMethods();  #--> Static method invoked using class 

