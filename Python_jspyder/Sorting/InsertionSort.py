class Solution:

    def insertionSort(self, arr):

        for i in range(1, len(arr)):

            key=arr[i]
            j=i-1
            print("for loop", j)

            while j>=0 and key<arr[j]:
                print("before arr[J+1]", arr[j+1])
                print("before arr[j]", arr[j])
                arr[j+1] = arr[j]

                print("after arr[J+1]", arr[j + 1])
                print("after arr[j]", arr[j])
                print("before while looop j value", j)
                j=j-1
                print("********* while loop j", j)

            print("before outer while looop a[j+1]", a[j+1])
            arr[j+1] = key
            print("after outer while looop a[j+1]", a[j + 1])

        return arr










s=Solution()
a=[8,4,1,3,2]
print(s.insertionSort(a))