

class JPattern:

    def jClassic(self):

        n=int(input("Enter the number \n"))

        for i in range(n):
            for j in range(n):

                if i==0 or j==n//2 or (i==n-1 and j<=n//2) or (i>=n//2 and j==0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()



    def jPattern(self):

        n=int(input("Enter the number \n"))

        for i in range(n):
            for j in range(n):

                if i==0 or j==n//2 or (i==n//2+j and j>=0 and j<=n//2) :
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()



j=JPattern()
j.jClassic()

j.jPattern()

