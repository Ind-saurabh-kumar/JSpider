# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:03:37 2024

@author: saura
"""

class FileHandling:
    
    def writeRead(self):
        
        try:
            file=open('new.txt','a+') 
            
            file.write("Saurab hKumar from jspider")
            
            file.seek(0)
             
            data=file.read()
            print(data)
        
        except FileNotFoundError:
            print("File not exist.....")
        
        
        finally:
            file.close()

f=FileHandling()
f.writeRead()
        
        
         