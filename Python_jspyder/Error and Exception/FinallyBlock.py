# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:14:49 2024

@author: saura
"""



class TestFinally:
    
    def displayFinallyClause(self, a,b):
        
        try:
            c=a/b
            print(c)
            
        except ZeroDivisionError:
            print("Denominator should not be equal to 0")
            
        finally:
            print("**********Does not matter what ever executed***")



t=TestFinally()
t.displayFinallyClause(10, 0)