class SlectionSort:

    def sortAlgo(self):

        a=[19,9,2,8,20,1]
        print(a)


        for i in range(len(a)):
            min=i
            for j in range(i+1,len(a)):
                if a[min]>a[j]:
                    min=j


            a[min], a[i] = a[i], a[min]

            print(a)




















        print(a)


sl=SlectionSort()
sl.sortAlgo()