class Solution:

    def specialDigit(self, num):
        ele=[]
        if num  <1:
            print("Number is not Defiend")
        else:
            for i in range(1, num+1):
                temp=i
                tsum=0
                tmult=1
                while temp!=0:
                    r=temp%10
                    # print(r)
                    tsum+=r
                    # print(tsum)
                    tmult*=r
                    # print(tmult)
                    temp = temp // 10
                if (tsum+tmult)==i:
                    ele.append(i)
        print(ele)




s=Solution()
n=int(input("Enter the Number \n"))
s.specialDigit(n)


