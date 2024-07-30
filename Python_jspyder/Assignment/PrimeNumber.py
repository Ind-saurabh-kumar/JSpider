# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:50:16 2024

@author: saura
"""


class PrimeNumber:
    
    def numPrime(self):
        
        num=int(input("Enter the Number: \n"))
        
        if num<=1:
            print("Enter the number greater than 1")
            
        for i in range(2, num):
            
            if num%i==0:
                print(f"{num} is not Prime Number ..")
                break;
            else:
                print(f"{num} is Prime Number ..")
                break;
            
            
                


pn=PrimeNumber()
pn.numPrime() 
            
    