

class ReverseWord:

    def wordRev(self):

        sentence = input("Enter you sentace here \n")
        reverseword= ""
        word = ""

        for i in sentence:
            if i != ' ':
                word = i + word
            else:
                reverseword += word + ' '
                word = ""

        reverseword += word


        print(reverseword)


rw=ReverseWord()
rw.wordRev()
