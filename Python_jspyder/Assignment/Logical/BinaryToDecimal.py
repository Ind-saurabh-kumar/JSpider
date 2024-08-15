
class BinaryToDecimal:

    def btd(self):
        binary=input("Enter the binary digits: \n")

        length=len(binary)
        decimal=0

        for i in binary:
            decimal+= int(i) * 2**(length-1)
            length=length-1

        return decimal

bd=BinaryToDecimal()
print(bd.btd())

