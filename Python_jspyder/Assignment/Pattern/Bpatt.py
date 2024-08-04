

class Bpatt:
    def classicB(self):

        n= int(input("Enter the number : \n"))

        for row in range(n):

            for col in range(n):

                if row==0 or col==0 or col==n-1 or row==n-1 or row==n//2:
                    print("*", end=" ")
                else:

                    print(" ", end=" ")
            print()

    def smoothB(self):

        n=int(input("Enter the number : \n"))

        for row in range(n):
            for col in range(n):

                if (row==0 and col<n-2) or (row==n//2 and col<n-2) or (row==n-1 and col<n-2) or col==0 or (col==n-1 and row>=2 and row<=n//2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()










b=Bpatt()
# b.classicB()
b.smoothB()