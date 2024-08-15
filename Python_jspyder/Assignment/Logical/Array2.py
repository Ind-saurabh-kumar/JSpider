

class Soluton:

    def arrMatch(self):

        l=5
        arr=[1,5,7,9,11]
        arr1=[1,5,2 ,8,10]
        arr2=[]

        for i in range(l):

            if arr[i]==arr1[i]:
                e=arr[i]
                arr2=e
                continue
            else:
                t=arr[i]-arr1[i]
                arr2=arr1[i]+t

        if arr==arr2:
            print("Match")
        else:
            print("Not Matching")



s=Soluton()
s.arrMatch()




