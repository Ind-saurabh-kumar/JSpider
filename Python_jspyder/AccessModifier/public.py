class Father:

    __abc=100   # private variable 

    def __smoke(self):    # private method
        print("Smoking")
    

    def checkBehaviour(self):
        self.__smoke()
        print(Father.__abc)



class Son(Father):

    pass 

f=Father()
f.checkBehaviour()


s=Son() 
s.checkBehaviour()