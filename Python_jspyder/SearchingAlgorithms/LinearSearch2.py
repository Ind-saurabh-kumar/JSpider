
class LinearSearch2:

    def linearSearch(self, arr, key):

        for i in range(0, len(arr)):
            if arr[i]==key:
                return i
            else:
                continue
        return -1


arr=[1,2,3,9,45,6,7]9
key=int(input("Enter the element \n"))
l=LinearSearch2()
res=l.linearSearch(arr, key)
if res==-1:
    print("No element found here")
else:
    print("Element found at ", res)