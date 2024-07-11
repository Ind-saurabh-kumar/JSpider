from abc import ABC, abstractmethod

class LoginPage(ABC):
    
    @abstractmethod
    def login(self):
        pass 
    
    

class Youtube(LoginPage):
    
    def login(self):
        print("Login Successfully .....")
        print("Enjoy the Contenct...")



class Whatsapp(LoginPage):
    
    def login(self):
        print("Login Success....")
        print("Start Chat")
        


y=Youtube()
y.login()

w=Whatsapp()
w.login()