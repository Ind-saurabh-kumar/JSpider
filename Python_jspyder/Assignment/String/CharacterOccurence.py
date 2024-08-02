class CharOccur:

    def occerChar(self):

        word= input("Enter the Word \n")
        newWord=""

        count=0

        for i in word:
            if i not in newWord:
                newWord+=i
            else:
                pass

        for n in newWord:

            for f in word:

                if n==f:
                    count+=1
                else:
                    p

            print(f"{n} occurs in word {count} times.")
            count=0

co=CharOccur()
co.occerChar()



