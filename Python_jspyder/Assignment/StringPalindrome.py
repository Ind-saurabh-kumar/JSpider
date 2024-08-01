
class StringPalindrome:

    def palindromeStr(self):

        word= input("Enter the word \n")
        word=word.upper()
        newStr=""

        for i in word:
            newStr= i+newStr

        if newStr==word:

            print("String is Palindrome...")
        else:
          print("String is not Palindrome...")


sp=StringPalindrome()
sp.palindromeStr()