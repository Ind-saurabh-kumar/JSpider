# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:50:16 2024

@author: saura
"""


class PrimeNumber:
    
    def numPrime(self, n):

        if n<1:
            print("Enter the number greater than or equal to 1")
        
        elif n==1:
            print(f"{n} is prime number")
            
        else:
            
            for i in range(2, n):
                
                if n%i==0:
                    return False
                    
            else:
                return True
        
        
    def isPrime(self):
        
        num=int(input("Enter the number:"))
        
        if self.numPrime(num):
            print(f"{num} is prime number")
        
        else:
            print(f"{num} is not prime.")
            
                


pn=PrimeNumber()
pn.isPrime()
            
    