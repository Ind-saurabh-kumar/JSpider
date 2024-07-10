# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:40:02 2024

@author: Saurabh Kumar
"""

class LocalVariable:
    
    def __init__(self):
        
        color="red"       # --> Local Variable of method
        print(color)
    
    def localVar(self):
        color="yellow"  # --> Local Variable of method
        print(color)
        
        x=int(input("Enter a number here:"))
        
        if(x>10):
            y=x*x;   # --> Local variable of blocks
            print(f"Local variable of if blocks {y}")
        
        else:
            y=x*2    # --> local variable of else block
            
            print(f"Local variable of else block {y}")
            
            
            
    
local=LocalVariable()

local.localVar()

        