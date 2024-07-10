# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:31:56 2024

@author: saura
"""


#creating class College
class College:
    def campus(self):  # it will give output when its callled
        print("Camp")

    def campus2(self):  # it will  give output when we call it in print function
        self.name = "Camp2"
        return self.name
    
    def salary(self):   # It is salary fuction which all will get
        self.sal = 20000
        return self.sal
    

class Bonus:      # It a commisson class it will not inherit any property because, Its occurs for some one only not for all the classes.
    def commision(self):
        self.com=10000
        return self.com
    

class Principal(College):  # Its inheriating the property of "College" then we can say that it is a "Single Level Inheritance"
    def teach(self):
        print("Teaching ")



class Teacher(Principal):  # It is inheriationg the proerty of "Principal"  as well as "College" indirectly  So, it is a "MUltilevel Inheriatance"
    def inviglator(self):
        print("They can guide in the exam. hall")


# NOTE:-  "AsstProf" and  "Principal" both are the derived class of "College " So, It is a  "Hierarchical inheritance "


class AsstProf(College, Bonus): # this class is inheriting the property of "College" and "Bonus" directly that's why It is called multiple Inheritance.
    def assist(self):
        self.help="Asst. Prof. always works under Professor"
        return self.help
    

print("**************** College Data ************************")
#object of  college class
c=College()
c.campus()    # Directly, I called it because It prints the output from methond
print(c.campus2())# Here, I used print function because I have to take output from method.
print(c.salary())

print("**************** Principal Data ************************")
# object of Principal
p=Principal()
p.teach()
# Its inherit the propety of college as well so I can call all the method with reference of principal object
p.campus()
print(p.campus2())
print(p.salary())


print("**************** Teacher Data ************************")
# object of Teacher
t=Teacher()
t.inviglator()
#Its inherit the propety of principal and  college so I can call all the method with reference of teacher object
t.campus()
print(t.campus2())
print(t.salary())
t.teach()  # it is principal property


print("**************** Asst. Prof. data ************************")
# object of  Asst. Prof.
a=AsstProf()
print(a.assist())

#Its inherit the propety of College and  Bonus so I can call all the method with reference of teacher object
a.campus()
print(a.campus2())
print(a.salary()) 
# Here, commsion geting only asst. prof.  for there assist tips. or no any other class getting bonus except asst. prof.
print(a.commision())

print("**************** Bonus data ************************")
# object of  Asst. Prof.
b=Bonus()
print(b.commision())










        






