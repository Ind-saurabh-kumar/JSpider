
from abc import ABC,abstractmethod

class Switch(ABC):
    
    @abstractmethod
    def turnOn(self):
        pass


class Light(Switch):
    
    def turnOn(self):
        print("Light: Turned On ........")



l=Light()
l.turnOn()