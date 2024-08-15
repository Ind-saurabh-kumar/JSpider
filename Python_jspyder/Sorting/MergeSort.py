

class Solution:

    def merge_sort(self, arr):
        orgArr=arr;

        if len(orgArr)>1:

            mid=len(orgArr)//2
            leftlist=orgArr[:mid]
            # print("first left", leftlist)
            rightlist=orgArr[mid:]

            # print("first right", rightlist)


            # print("left",leftlist)
            # print("right", rightlist)

            self.merge_sort(leftlist);
            self.merge_sort(rightlist)

            print("leftlist length", leftlist)
            print("length of right", rightlist)

            i=0
            j=0
            k=0

            while i<len(leftlist) and j<len(rightlist):


                if leftlist[i] < rightlist[j]:
                    # print("************* left list ",i, len(leftlist))
                    # print("************ rightlist ",j, len(rightlist))
                    orgArr[k]=leftlist[i]

                    i+=1

                else:
                    orgArr[k]=rightlist[j]
                    j+=1

                k+=1

            # Remainaing element in left list
            while i<len(leftlist):
                # print("left rem",leftlist)
                orgArr[k] = leftlist[i]
                i+=1
                k+=1


            # Remaining element in right list
            while j<len(rightlist):
                # print("right rem", rightlist)
                orgArr[k] = rightlist[j]
                j+=1
                k+=1













m=Solution()

list=[75,29,83,42,16]
print("original list", list)
m.merge_sort(list)

print("After sorted list", list)

