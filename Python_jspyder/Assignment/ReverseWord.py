

class ReverseWord:

    def wordRev(self):

        sen= input("Enter the String...\n")

        revStr= ' '
        cW = ""

        for i in sen:

            if i!= ' ':
                cW = cW +i

            else:
                revStr = " "+cW +revStr
                cW=' '
        revStr = cW+ ' ' +revStr
        print(revStr)


rW=ReverseWord()
rW.wordRev()

