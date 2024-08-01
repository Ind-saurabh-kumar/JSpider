

class ReverseWord:
    def wordRev(self):
        sen = input("Enter the String...\n")

        revStr = ''
        currWord = ''

        for i in sen:
            if i != ' ':
                currWord = currWord + i
            else:
                revStr = ' ' + currWord + revStr
                currWord = ''

        # Add the last word to the reversed string
        revStr = currWord + revStr
        print(revStr.strip())  # Strip any leading/trailing spaces

rW = ReverseWord()
rW.wordRev()