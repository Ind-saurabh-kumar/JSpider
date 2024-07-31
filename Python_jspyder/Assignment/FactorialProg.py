# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 23:42:53 2024

@author: saura
"""

class Factorial:
    
    def fact(self):
    
        
        
        number=int(input("Enter the Number...\n"))
        factorial = 1

        if number < 0:
            print("Enter positeve Number")
        else:
            for i in range(1, number + 1):
                factorial = factorial*i

            print(f"The factorial of {number} is {factorial}")
    
f=Factorial()
f.fact()
                