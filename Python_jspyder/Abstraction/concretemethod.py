# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:03:01 2024

@author: saura
"""

from abc import ABC, abstractmethod 

class Switch(ABC):
    
    @abstractmethod
    def turnOn(self): # abstract method
        pass 
    
    
    def turnOff(self): # concrete method
        print("Turned off ......")
    
    


class Light(Switch):
    
    def turnOn(self):
        print("Light :- Turned On")



l=Light()
l.turnOn()
l.turnOff()