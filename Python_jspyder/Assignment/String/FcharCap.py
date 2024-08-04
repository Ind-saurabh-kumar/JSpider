class FirstCharUpper:

    def upperChar(self):
        sen = input("Enter the String: \n")
        newSen = ""
        count = 0

        for i in sen:
            count += 1
        # print(count)

        for j in range(count):
            if j == 0:
                asc = ord(sen[0])
                # print(asc)

                if asc >= 65 and asc <= 90:
                    newSen += sen[0]
                    # print(newSen)
                else:
                    newSen += chr(asc - 32)
            elif sen[j] == ' ' and j + 1 < count:
                asc = ord(sen[j + 1])
                if asc >= 65 and asc <= 90:
                    newSen += " " + sen[j + 1]
                    # print(newSen)
                    # print("elif if block")
                else:
                    newSen += " " + chr(asc - 32)
                    # print(newSen)
                    # print("elif else ")
            else:

                newSen += sen[j]
                # print(newSen)
                # print(" else ")

        print(newSen)

fcu = FirstCharUpper()
fcu.upperChar()
