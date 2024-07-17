# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:49:31 2024

@author: saura
"""


class IndexExceptionCheck:
    
    def checkIndex(self):
        a = [1,2,3,4]
        try:
            print(a[5])
        except IndexError:
            print("Index is out of bound")


i=IndexExceptionCheck()
i.checkIndex()