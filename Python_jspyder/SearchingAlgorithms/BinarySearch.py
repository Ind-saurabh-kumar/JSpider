
class Solution:

    def binarySearch(self, key):
        arr= [1, 2, 4, 5, 6, 7, 8, 9, 12, 14, 15]
        low = 0
        high = len(arr) - 1
        print(high,"high")
        print(low, "low")

        while low<high:


            mid=(low+high)//2
            if mid==0:
                mid=mid+1
            print(mid, "mid value")


            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                low=mid+1
            else:
                high=mid-1


        return -1


s=Solution()


key=8

res=s.binarySearch(key)

if res==-1:
    print(f"{key} --> Does not found...")

else:
    print(f"{key} found at {res} index.....")





