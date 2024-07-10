# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:06:07 2024

@author: Saurabh Kumar
"""

class Father:
    
    def drive(self):
        print("father driving.")
        


class Mother:
    def cook(self):
        print("Coocking")
    
    def drive(self):
        print("Driving mother")
        


class Son(Mother,Father):
    def ride(self):
        print("riding")
        



F=Father()
F.drive()


print("********* Mother ***********")


M=Mother()
M.cook()


print("********* Mother ***********")

s=Son 
s.drive()
s.ride()


    
    