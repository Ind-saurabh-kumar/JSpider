class Solution:

    def armStrongNum(self, num):
        count=0
        n=num
        while n!=0:
            # n%10
            count+=1
            n=n//10
            # print(count)
        tsum=0
        for i in str(num):
            tsum+=int(i)**count
        if tsum==num:
            return True
        else:
            return False

s=Solution()

n=int(input("Enter the number \n"))
res=s.armStrongNum(n)

if res ==True:
    print(f"{n} -->Number is an ArmStrong....")

else:
    print(f"{n} -->Number is not an ArmStrong....")




