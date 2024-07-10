# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:26:04 2024

@author: Saurabh Kumar
"""

class Animal:
    
    x=10
    
    def eat(self):
        print("Animals are eat.....")
 
        


class Dog(Animal):
    
    def bark(self):
        print("Barking.......")
        
        
A=Animal()
A.eat()



D=Dog()
D.eat() 
D.bark()