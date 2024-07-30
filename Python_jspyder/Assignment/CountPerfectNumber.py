# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:14:16 2024

@author: saura
"""

class CountPftN:
    
    
    def countPFN(self):
        
        n= int(input("Enter the number: \n"))
        
        
        
        for num in range(1, n+1):
            
            sum=0
            
            for div in range(1, num):
                
                if num%div==0:
                    sum = sum+div
            
            
            if sum==num:
                print(f"{num} is perfect number prsent between 1 and {n}..")


cpftn=CountPftN()
cpftn.countPFN()