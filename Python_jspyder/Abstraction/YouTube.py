from abc import ABC, abstractmethod

class Login(ABC):
    
    @abstractmethod
    def login(self):
        pass
    
    def logout(self):
        print("Logout")
        
class Youtube(Login):
    def login(self):
        print("Youtube Login Successfully")
        


y=Youtube()
y.login()
y.logout()