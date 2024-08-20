
class Solution:

    def desariumNum(self, num):

        count=0
        n=num
        while n!=0:
            count+=1
            # print(count)
            n=n//10

        tsum=0
        temp=num
        while count >=1 and temp!=0:
            if count>0:
                r=temp%10
                tsum += r**count
                print(f"power={count}, {r}**{count} = {r**count} sum={tsum}")
                temp=temp//10
            count=count-1

        if num==tsum:
            print(f"{num} --> is a Desarium Number.")
        else:
            print(f"{num} --> is not a Desarium Number.")


s=Solution()
n=int(input("Enter the Number \n"))
s.desariumNum(n)






