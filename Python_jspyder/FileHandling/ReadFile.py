# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:16:27 2024

@author: saura
"""


class FileHandling:
    
    def readFile(self):
        
        file=None
        
        try:
            file=open('his.txt', 'r' )
            
            d=file.read()
            print(d)
            

        
        except FileNotFoundError:
            print("file does not exist..")
        
        finally:
            try:
                if file is not None:
                    file.close()
                    print("file is closed")
            
            except FileNotFoundError:
                pass
        
    
            
        

f=FileHandling()
f.readFile()