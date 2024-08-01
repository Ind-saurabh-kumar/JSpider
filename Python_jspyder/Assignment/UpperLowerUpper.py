

class UpperLowerLower:

    def upprLowerUppr(self):

        word = input("Enter the wordf \n")

        for i in word:

            ascii=ord(i)
            newWord=""
            if (ascii >= 65 and ascii <= 90):
                newWord += chr(ascii+32)
            else:
                newWord += chr(ascii-32)
            print(newWord, end="")

ullu=UpperLowerLower()
ullu.upprLowerUppr()