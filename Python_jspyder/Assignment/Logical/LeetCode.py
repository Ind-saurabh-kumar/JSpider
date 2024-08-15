class Solution:

    def solWhile(self):

        inpStr=input("Enter the string here: \n")
        resStr=''
        for i in range(len(inpStr)):
            char=inpStr[i]
            count=0

            while(i+1<len(inpStr)) and inpStr[i].isdigit():
                count=count*10+int(inpStr[i])
                i=i+1


            resStr+=char*count
        print(resStr)


    def solFor(self):
        inpStr = input("Enter the string here: \n")
        resStr = ''

        for i in range(len(inpStr)):
            char = inpStr[i]
            count = 0

            for j in range(i + 1, len(inpStr)):
                if inpStr[j].isdigit():
                    count = count * 10 + int(inpStr[j])
                else:
                    break

            resStr += char * count

        print(resStr)

s=Solution()
s.solFor()