class BubbleSort:

    def sol(self):

        a=[1,23,4,5,7]

        for i in range(len(a)):

            for j in range(i+1, len(a)):

                if a[j]<= a[i]:
                    a[j]=a[j]+a[i]-a[j]
                    a[i]=a[j]  


        print(a)



b=BubbleSort()
b.sol()


