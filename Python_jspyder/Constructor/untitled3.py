# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:17:42 2024

@author: Saurabh Kumar
"""

class Animal:
    def eat(self):
        print("All animals eat") 
        
a=Animal()
a.eat()

class Dog(Animal):
    pass 

d=Dog
d.eat()