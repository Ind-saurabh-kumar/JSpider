# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:40:39 2024

@author: Saurabh Kumar
"""

class Product:
    
    def __init__(self):
        self.productId = 101
        self.productName = "Mobile"
    
    
    def __init__(self, productId,productName):
        self.productId = productId
        self.procutName= productName 
        
    
    def __init__(self, productId, productName, productPrice):
        self.productId = productId
        self.productName = productName 
        self.productPrice = productPrice 
        
p=Product(103,"Dress",10000)
print(p.productId, p.procutName, p.productPrice) 