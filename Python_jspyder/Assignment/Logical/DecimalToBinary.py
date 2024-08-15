

class DecimalToBinary:

    def dtb(self):

        n=int(input("Enter the number:"))
        bin=""
        rbin=""

        if n==0:
            bin +=str(0)
        else:
            while n!=0:
                bin+=str(n%2)+""
                n=n//2

        print(bin)
        for i in bin:
            rbin=i+rbin

        print(rbin)



b=DecimalToBinary()
b.dtb()

