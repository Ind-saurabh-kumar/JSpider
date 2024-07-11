
from abc import ABC, abstractmethod

class Switch(ABC):
    
    @abstractmethod
    def turnOn(self):
        x=10
        if(x>20):
            print("Not Valid")
         
        else:
             print("Valid") 
    
        print(".>>>>>>>>>>") 
        print("...........")
        print(".........")
    

class Light(Switch):
    
    def turnOn(self):
        print("Light :- turned on........ ");



light=Light()
light.turnOn()
      