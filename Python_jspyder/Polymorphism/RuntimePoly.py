# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:48:51 2024

@author: saura
"""

class Switch:
    
    def turnOn(self):
        print("Switch: Turn On ......")
        
    def turnOff(self):
        print("Switch: Turn Off ......")
        

class Light(Switch):
    
    def turnOn(self):
        print("Light: Turn On .....")
        


light = Light()
light.turnOn()