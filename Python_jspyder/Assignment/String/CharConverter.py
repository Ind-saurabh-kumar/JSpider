

class CharConvert:

    def conChar(self):

        word= input("Enter the Word: \n")

        word.lower()
        uppr=""

        for i in word:
            ascii=ord(i)
            uppr+=chr(ascii-32)

        print(uppr)

cc=CharConvert()

cc.conChar()

