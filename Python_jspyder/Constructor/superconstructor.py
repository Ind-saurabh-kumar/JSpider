# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:45:52 2024

@author: saura
"""



class AnimalType:
    
    def __init__(self, animalType):
        print(" Animal type is", animalType)
    
    
    def eat(self):
        print("Eating.........")

class Dog(AnimalType):
    
    def __init__(self):
        print("I am Dogs Constructor....")
    
        super().__init__("Herbibores")
    
    
    def dogsBehaviour(self):
        super().eat()


d=Dog()
d.dogsBehaviour()
