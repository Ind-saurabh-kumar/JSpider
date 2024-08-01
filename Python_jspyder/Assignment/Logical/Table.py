# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:56:47 2024

@author: saura
"""



class Table:
    
    def table(self):
        
        n= int(input("Enter the number \n"))
        
        for i in range(1,11):
            
            res = n*i
            
            print(f" {n} * {i} = {res}" )
            


t=Table()
t.table()