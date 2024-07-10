# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:27:55 2024

@author: Saurabh Kumar
"""

class Product:
    
    def __init__(self, productId, productName):
        self.productId=productId;
        self.productName=productName;

p=Product(102, "Dress")
print(p.productId, p.productName)