class Solution:

    def armStrongNum(self, num):
        temp=num

        num=str(num)
        l=len(num)

        tsum=0
        for i in num:
            tsum+=int(i)**l


        if tsum==temp:
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




