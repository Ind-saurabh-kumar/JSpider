# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:09:22 2024

@author: saura
"""



class PerfectNum:
    
    def perfect(self):
        
        n= int(input("Enter the number \n"))
        sum=0
        
        for i in range(1,n):
            
            if n%i==0:
                
                sum +=i
        
        
        if sum==n:
           print(f"{n} is Perfect Number.... ")
         
            
        else:
            print(f"{n} is Not Perfect Number....")
            
pfn=PerfectNum()
pfn.perfect()