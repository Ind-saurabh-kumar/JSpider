# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:45:06 2024

@author: Saurabh Kumar
"""

class Node:
    
    def __init__(self, data= None, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next 
        
        

class CDLL:
    
    def __init__(self, start=None):
        self.start = start 
        
        
    def is_empty(self):
        return self.start==None
    
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
        
    def insert_at_last(self, data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n 
            self.start=n
        else:
            n.next=self.start 
            n.prev=self.start.prev 
            n.prev.next=n 
            self.start.prev = n 
            
            
            
    
    
    
    
    def printLL(self):
        temp=self.start
        if temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
            while temp is not self.start:
                print(temp.item,end=' ')
                temp=temp.next
        
        
        
            



c=CDLL()

print(c.is_empty())
c.insert_at_start(45)
c.printLL()


        
        