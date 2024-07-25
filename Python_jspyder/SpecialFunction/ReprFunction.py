

class Test:
    
    def __init__(self):
        
        self.name = "Saurabh"
        
        print("Object Created")
        
    
    def __repr__(self):
        return f'Object Name is Test and has var {self.name}'
    
    def __str__(self):
        return f'The value of name is {self.name} Vivek'
    


t=Test()

print(repr(t))
print(str(t))