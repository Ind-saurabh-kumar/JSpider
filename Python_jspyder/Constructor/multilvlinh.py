# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:37:19 2024

@author: Saurabh Kumar
"""

class Animal:
    x=10
    
    def eat(self):
        print("eating....")



class Dog(Animal):
    def bark(self):
        print("barking")
        
        

class BabyDog(Dog):
    def weep(self):
        print("Weeping..")
        


print("******************* Animal ************************************")
A=Animal()
A.eat()

print("********************** Dog ******************")


D=Dog()
D.eat() 
D.bark()

print("********************** Baby Dog ******************")
B=BabyDog()
B.x
B.eat()
B.bark()
B.weep()