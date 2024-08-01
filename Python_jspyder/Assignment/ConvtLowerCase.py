

class ConvtLowerCase:

    def lowerCase(self):

        word= input("Enter the Word in Capital letter \n")

        word=word.upper()
        lower=""
        for i in word:
            ascii = ord(i)
            lower += chr(ascii+32)

        print(lower)


cl=ConvtLowerCase()
cl.lowerCase()

