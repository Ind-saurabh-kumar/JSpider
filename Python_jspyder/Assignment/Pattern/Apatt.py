class Apattern:

    def clasicA(self):

        n = int(input("Enter the Number : \n"))

        for i in range(n):
            for j in range(n):

                if i==0 or i==n//2 or j==0 or j==n-1:
                    print("*", end=" ")

                else:
                    print(" ", end=" ")
            print()


    def smoothA(self):

        n= int(input("Enter the value of n :\n"))

        for row in range(n):
            for col in range(n):

                if (row==0 and col>=2 and col<n-2) or (row==1 and col==1) or (row==1 and col==n-2) or row==n//2 or (col==0 and row>=2) or (col==n-1 and row>=2):
                    print("*", end=" ")

                else:
                    print(" ", end=" ")
            print()

    def originalA(self):
        n= int(input("Enter the number : \n"))

        for row in range(n):

            for col in range(n-row +1):
                print(" ",end="")

            for s in range(2*row+1):

                if s==0 or s==2*row:
                    print("*", end="")
                elif (row==n//2+1):
                    print("*", end="")
                else:
                    print(" ", end="")


            print()

apatt=Apattern()
apatt.clasicA()
apatt.smoothA()

apatt.originalA()