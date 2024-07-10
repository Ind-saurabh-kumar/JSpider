# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:15:43 2024

@author: saura
"""

class Movie:
    
    def __init__(self, id, name, price):
        
        self.__movieId=id 
        self.__movieName=name 
        self.__moviePrice=price
        
        
    def getId(self):
        return self.__movieId
    
    def getName(self):
        return self.__movieName 
    
    def getPrice(self):
        return self.__moviePrice 
    
    
    def setId(self, id):
        self.__movieId = id 
        
    def setName(self, name):
        self.__movieName= name 
        
    def setPrice(self, price):
        self.__moviePrice 



m=Movie("1","Movie1",200)

print(m.getId())
print(m.getName())
print(m.getPrice())

m.setId("2")
m.setName("m2")
m.setPrice(300)
print("********* Updated Values  *********")
print(m.getId())
print(m.getName())
print(m.getPrice())