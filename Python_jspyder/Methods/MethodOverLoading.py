# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:25:03 2024

@author: Saurabh Kumar
"""

class Calculate:
    
    def add(self):  # It will give error because in python old defined method is not callable in method overloading
        x=10
        y=20
        z=x+y
        print(z)
        
    def add(self, a, b):  # 
        x=a
        y=b
        z=x+y
        print(z)
        
    
    def add(sef, b,a): # This method will execute only because it is lateset defined method in method overloading
        x=a
        y=b
        z=x+y
        print(z)
        

c=Calculate()
# c.add()            # we can't call it because it old method defined in the code
c.add(20, 30)