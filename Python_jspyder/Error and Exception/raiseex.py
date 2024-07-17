# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:16:53 2024

@author: saura
"""



class Vote:
    
    def ageValid(self, age):
        if (age<18):
            raise Exception("You are not allowed to vote...")
        
        else:
            print("Cong. you are allowed to vote....")


v=Vote()
v.ageValid(15)