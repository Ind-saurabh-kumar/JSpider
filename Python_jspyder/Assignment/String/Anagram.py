class Anagram:

    def anag(self):

        str1=input("Enter the String1 \n")

        str2=input("Enter the String2 \n")
        count1=0
        count2=0
        for i in str1:
            count1+=1
        for j in str2:
            count2+=1

        frq1=[]*26
        frq2=[]*26

        if count1==count2:

            for i in str1:
                frq1=[ord(i)-ord(a)+1]
                print(frq1)

            for j in str2:
                frq2 = [ord(i)-ord(a)+1]
                print(frq2)




        else:
            print("String is not Anagram")

a=Anagram()
a.anag()