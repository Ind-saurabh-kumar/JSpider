# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:06:59 2024

@author: saura
"""



class IndexExceptionCheck:
    
    def checkIndex(self):87
        a=[1,2,3,4]
        
        try:
            print(a[5])
        except IndexError:
            print("Index is out of bound")
        
        try: 
            z=10/0
            
            print(z)
        except BaseException:
            print("BaseException:- Denom should not be zero") 
        
        
        except ZeroDivisionError:
            print("Denominator can not be zero")
            

i=IndexExceptionCheck()
i.checkIndex()