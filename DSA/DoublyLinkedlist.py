# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:07:28 2024

@author: Saurabh Kumar
"""


# Node Creation 
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item 
        self.next = next 
        
  
# Doubly LinkedList Code 

class DoublyLinkedlist:
    
    # Creation of Linked List
    def __init__(self, start=None):
        self.start = start 
        
    
    # Empty Linked List 
    
    def is_empty(self):
        return self.start == None 
    
    # Insert at start 
    
    def insert_at_first(self, data):
        n = Node(None, data, self.start)
        
        if not self.is_empty():
            self.start.prev = n 
        self.start = n 
        
    # Insert at last 
    
    def insert_at_last(self, data):
        temp = self.start 
        if self.start != None:
            while temp.next is not None:
                temp = temp.next 
        
        n = Node(temp, data, None) 
        
        if temp == None: 
            self.start = n 
        
        else:
            temp.next = n 
            
            
    # Searching 
    
    def search(self, data):
        temp = self.start 
        
        while temp.next is not None:
            if temp.item == data:
                return temp 
            
            temp=temp.next 
        return None 
    
    
    # Insert after 
    
    def insert_after(self, temp, data):
        if temp is not None:
            n=Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n 
    
    # PrintList 
    
    def print_list(self):
        temp = self.start 
        
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            
    
    # Delete First 
    
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next 
            if self.start is not None: 
                self.start.prev = None 
    
    # Delete Last 
    
    def delete_last(self):
        if self.start is None:
            pass 
        elif self.start.next is None:
            self.start = None 
            
        else:
            temp = self.start 
            while temp.next is not None:
                temp = temp.next 
            temp.prev.next = None
            
    
    # Delete Element 
    
    def delete_item(self, data):
        if self.start is None: 
            pass
        else:
            temp = self.start 
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next 
                    else:
                        self.start = temp.next 
                    break 
                temp = temp.next 
        
     # Make LinkedList Iterable 
     
    def __iter__(self):
        return DoublyLinkedlistIterable(self.start)


class DoublyLinkedlistIterable:
    
    def __init__(self, start):
        self.current = start 
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        if not self.current:
            raise StopIteration 
        
        data = self.current.item 
        self.current = self.current.next 
        return data 
    
    
    
    
    
 # --------------------- Driver Code --------------------------------
 
 
mylist = DoublyLinkedlist()
 
mylist.insert_at_first(10)
mylist.print_list()
print()
mylist.insert_at_first(20)
mylist.print_list()
print()

mylist.insert_at_last(45)
mylist.print_list()
print()

mylist.insert_after(mylist.search(20),78)
mylist.print_list()

print()

for x in mylist:
    print(x)
    
print()

mylist.delete_first()
mylist.print_list()
print()

mylist.delete_last()
mylist.print_list()

print()

mylist.delete_item(78)
mylist.print_list()
 
    
    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    