# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:07:18 2024

@author: saura
"""

import math
class Packages:
    
    def piCal(self, number):
        
        a=number
        
        print(a*math.pi)
        
    def powCal(self, base, power):
        
        b=base
        p=power 
        
        print(math.pow(b, p))
    
    
    def factCal(self, number):
        
        n=number
        print(math.factorial(n))
        
        
        
p=Packages()
p.factCal(5)
p.powCal(5, 6)
p.piCal(6)
        