# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:12:20 2024

@author: saura
"""



class ListProg:
    
    def __init__(self):
        self.newList =[1,2,"saurabh",45.5, 8638869369, None, None]
        
        
        
    def dispaly(self):
        print(self.newList)
        
    
    def appendEle(self, num):
        print(f"Before appending elements in the list \n {self.newList}")
        
        self.newList.append(num)
        
        
        print(f"After appending elements in the list \n {self.newList}")

    def insertEle(self, position, num):
        print(f"Before inserting elements in the list \n {self.newList}")
        
        self.newList.insert(position, num)
        
        
        print(f"After inserting elements in the list \n {self.newList}")
        
        
    def removeEle(self, num):
        print(f"Before removing elements in the list \n {self.newList}")
        
        self.newList.remove(num)
        
        
        print(f"After removing elements in the list \n {self.newList}")
        
    
    def conStrList(self, string):
        name=string
        print(f"Before removing elements in the list \n {name} ")
        
        name=list(name)
        
        
        print(f"After removing elements in the list \n {name}")
        
    
    def lengthFun(self):
        
        print(f"No. of elements present in the list \n {self.newList}")
        
    
    def splitFun(self):
        
        sen = input("Please enter your String here. \n")
        
        sen = sen.split()
        
        print(sen)
        
        
    def posSlice(self):
        
        start = int("Enter starting point")
        stop = int("Enter ending point")
        step=int("Pass how many steps you want to go for, if not pass zero 0")
        
        if step ==0: 
            print(f"original elements in the list \n {self.newList}")
            
            res=self.newList[start:stop:step]
            
            
            
            print(f"After geting elements in the list \n {res}")
        
        else:
            
            print(f"original elements in the list \n {self.newList}")
            
            res=self.newList[start:stop]
            
            
            print(f"After geting elements in the list \n {res}")
            
    
    
    def negSlice(self, start, stop, step=None):
        print("Pass only integer values here ")
        start = int("Enter starting point")
        stop = int("Enter ending point")
        step=int("Pass how many steps you want to go for, if not pass zero 0")
        
        if step ==0: 
            print(f"original elements in the list \n {self.newList}")
            
            res=self.newList[start:stop:step]
            
            
            
            print(f"After geting elements in the list \n {res}")
        
        else:
            
            print(f"original elements in the list \n {self.newList}")
            
            res=self.newList[start:stop]
            
            
            print(f"After geting elements in the list \n {res}")
            print(f"After geting elements in the list \n {res}")
        
    
    def printList(self):
        
        for i in self.newList:
            print(i)
    
    
    def oddEle(self):
        
        for i in self.newList:
            if i%2!=0:
                print(i)
                
    def evenEle(self):
        
        for i in self.newList:
            if i%2==0:
                print(i)
                
    
    
        
        
    
        
        
        
        
l=ListProg()

l.dispaly()

l.lengthFun()

l.appendEle(25)

l.insertEle(5, 45)

l.removeEle(25)

l.printList()

l.oddEle()

l.evenEle()

try:
    l.posSlice(1, 5)
except IndexError:
    print("Not present in the list, range out of list")
    
    
try:
    l.negSlice()
except IndexError:
    print("Not present in the list, range out of list")
    

l.splitFun()




        
    
        
        
    
        