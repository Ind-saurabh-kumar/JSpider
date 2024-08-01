# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:31:12 2024

@author: saura
"""



class findVowel:
    
    def vowel(self):
        
        name=input("Enter Your Name Please.\n")
        
        
        vowel="aeiou"
        
        fount=[]
        
        
        for i in name:
            if i in  vowel:
                fount.append(i)
        
        print(fount)
                
                


v=findVowel()

v.vowel()