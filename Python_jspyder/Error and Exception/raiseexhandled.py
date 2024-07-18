# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:03:31 2024

@author: saura
"""



class InvalidAgeException(BaseException):
    
    def __init__(self):
        message = "Age is not valid for vote ..."
        
        # handled the raised exception
        super().__init__(message)


class CheckAge:
    
    def validAge(self, age):
        
        if age<18:
            
            raise InvalidAgeException 
        
        else:
            print("Your age is valid for vote...")



c=CheckAge()
c.validAge(15)