
class SPattern:

    def pattS(self):

        n = int(input("Enter the number: \n"))

        for i in range(n):

            for j in range(n):

                if i==0 or i==n//2 or i==n-1 or (j==0 and i<n//2) or (j==n-1 and i>n//2):
                    print("*", end=' ')

                else:
                    print(" ", end=" ")

            print()

s=SPattern()
s.pattS()
