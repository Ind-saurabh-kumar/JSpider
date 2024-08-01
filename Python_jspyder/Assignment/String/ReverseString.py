

class ReverseSen:

    def senReverse(self):

        name= input("Enter Your sentence here;\n ")
        count=0
        reverseSen=""
        for i in name:
            reverseSen = i +  reverseSen

        print("Revesed Sentence is.....\n")
        print(reverseSen)




rs=ReverseSen()
rs.senReverse()