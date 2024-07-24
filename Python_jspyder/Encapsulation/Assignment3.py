

import re

class InvalidEmailId(BaseException):
    
    def __init__(self):
        message="Invalid Email Id"
    
        super().__init__(message)
        

class InvalidPassword(BaseException):
    
    def __init__(self):
        message="Invalid Password.."
        super().__init__(message)
        

class Email:
    
    def enterEmail(self, email):
        
        email=email.lower()
        
        pattern = r'^[a-z0-9._%+-]+@gmail\.com$'
    
        # Match the email with the pattern
        if re.match(pattern, email):
            print("Valid Email Id")
            
            print("\n")
        else:
            raise InvalidEmailId()
            
class Password: 
    def enterPassword(self, password):
        
        pattern = r'^[a-zA-Z._%+-]+[0-9]$'
        
        
        if re.match(pattern, password):
            print("Valid Password")
            
        else:
            raise InvalidPassword()
        
        
        
        
        
        
   

e=Email()
try:
    e.enterEmail("Saurabhk@gmail.com")  

except InvalidEmailId:
    print("Invalid Email Id")


p=Password()
try:
    p.enterPassword('4587')
except InvalidPassword:
    print("Invalid Password....")