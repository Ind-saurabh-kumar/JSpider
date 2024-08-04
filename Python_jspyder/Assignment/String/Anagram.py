class Anagram:

    def anag(self):

        str1 = input("Enter the String1 \n").lower()
        str2 = input("Enter the String2 \n").lower()

        count1 = 0
        count2 = 0

        for i in str1:
            count1 += 1
        for j in str2:
            count2 += 1

        if count1 != count2:
            print("String is not Anagram")
            return

        frq1 = {}
        frq2 = {}

        for i in str1:
            if i in frq1:
                frq1[i] += 1
                print(frq1)
            else:
                frq1[i] = 1
                print(frq1)

        for j in str2:
            if j in frq2:
                frq2[j] += 1
                print(frq2)
            else:
                frq2[j] = 1
                print(frq2)

        print(type(frq1))
        print(type(frq2))

        if frq1 == frq2:
            print("Anagram")
        else:
            print("String is not Anagram")

a = Anagram()
a.anag()
