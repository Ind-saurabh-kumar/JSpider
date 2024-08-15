
class OctalToDecimal:

    def btd(self):
        binary=input("Enter the binary digits: \n")

        length=len(binary)
        decimal=0

        for i in binary:
            decimal+= int(i) * 8**(length-1)
            length=length-1

        return decimal

bd=OctalToDecimal()
print(bd.btd())

