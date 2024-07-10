# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Shop:
    
    def __init__(self):
        self.__shopId="s1"
        self.__shopName="Shop1"
        self.__shopRent=30000
    
    
    def getId(self):
        return self.__shopId
    
    
    def getName(self):
        return self.__shopName
    
    
    def getPrice(self):
        return self.__shopRent
    
    
    def setId(self, id):
        self.__shopId=id 
    
    def setName(self, name):
        self.__shopName=name
    
    def setPrice(self, rent):
        self.__shopRent= rent
        
        
s=Shop()

print(s.getId())
print(s.getName())
print(s.getPrice())


s.setId("s101")
s.setName("shop 100")
s.setPrice(20000)

print("***** Updated the value ******")
print(s.getId())
print(s.getName())
print(s.getPrice())


        