
class SenUpprLwr:

    def upprLwrSen(self):

        sen=input("Enter the sentence: \n")
        newStr=''

        for i in sen:

            if i == ' ' or i=='.':
                newStr +=i
            else:
                ascii=ord(i)
                if (ascii >= 65 and ascii <=90):
                    newStr += chr(ascii+32)
                else:
                    newStr += chr(ascii-32)

        print(newStr)

s=SenUpprLwr()
s.upprLwrSen()

