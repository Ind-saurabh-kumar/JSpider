# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:13:40 2024

@author: saura
"""



class PalindromeNum:
    
    def palinNum(self):
        
        num = int(input("Enter the Number.. \n"))
        
        temp=num 
        
        rev=0
        
        while(num!=0):
            
            r=num%10
            
            rev= rev*10+r
            
            num=num//10
        
        
        if temp==rev:
            print(f"{temp} is palindrome...")
        
        
        else:
            print(f"{temp} is not palindrome... ")
            
p=PalindromeNum()
p.palinNum()
            
            
            