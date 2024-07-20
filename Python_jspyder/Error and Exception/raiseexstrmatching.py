# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:00:12 2024

@author: saura
"""



class StringMissMatching(BaseException):
    
    
    def __init__(self):
        
        message="String is not Matching..."
    
        super().__init__(message)


class StrMatch:
    
    def strm(self,a,b):
        a=a.lower()
        b=b.lower()
        if a!=b:
            raise StringMissMatching()
        else:
            print("Both String are Same......")
    
    
s=StrMatch()
s.strm("Apple1", "apple4")

  
                            
        
                