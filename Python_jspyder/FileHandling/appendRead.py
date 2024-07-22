# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:03:37 2024

@author: saura
"""

class FileHandling:
    
    def appendRead(self):
        
        try:
            file=open('new.txt','a+') 
            
            file.write("Saurab hKumar from jspider")
            
            file.seek(0)
             
            data=file.read()
            print(data)
        
        except FileNotFoundError:
            print("File not exist.....")
        
        
        finally:
            try:
                if file is not None:
                    file.close()
                    print("file is closed")
            
            except FileNotFoundError:
                pass

f=FileHandling()
f.appendRead()
        
        
         