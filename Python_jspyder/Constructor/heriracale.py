# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:52:20 2024

@author: Saurabh Kumar
"""

class Animal:
    x=10 
    def eat(self):
        print("Eating..")
    
class Dog(Animal):
    def bark (self):
        print("Barking ......")


class Cat(Animal):
    def meow(self):
        print("meowing ....")


class Lion(Animal):
    def roar(self):
        print("roaring.....")
        
        

print("******************* Animal ************************************")
A=Animal()
A.eat()

print("********************** Dog ******************")


D=Dog()
D.eat() 
D.bark()

print("********************** Baby Dog ******************")
B=Cat()
B.x
B.eat()
B.meow()

print("********************** Lion ******************")
L=Lion()
L.x
L.eat()
L.roar()


