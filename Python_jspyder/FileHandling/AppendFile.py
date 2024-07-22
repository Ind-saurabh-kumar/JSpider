# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:16:27 2024

@author: saura
"""


class FileHandling:
    
    def appendFile(self):
        
        file=None
        
        try:
            file=open('hh.txt', 'a' )
            
            file.write("It is for writing code only....")
            print("Data appended....")
            
            
        
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
f.appendFile()