
class PmidNumAddPatt:
    def numAdd(self):

        n= int(input("Enter the number: \n"))

        for i in range(n):
            for j in range(n-i):
                print(" ", end=" ")
            num=1
            for k in range(i+1):
                print(num, end='')

                num = num*(i-k)//(k+1)

                if k<i:
                    print("  ", end='')

            print()

pna=PmidNumAddPatt()
pna.numAdd()
