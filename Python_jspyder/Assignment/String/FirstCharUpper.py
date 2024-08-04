class FirstCharUpper:
    def upperChar(self):
        sen = input("Enter the String: \n")

        newSen = ""
        length = 0

        # Calculate the length of the input string
        for char in sen:
            length += 1

        # Iterate through the string and capitalize as needed
        for i in range(length):
            if i == 0 or (i > 0 and sen[i - 1] == ' '):
                asc = ord(sen[i])
                if 97 <= asc <= 122:  # Check if it is a lowercase letter
                    newSen += chr(asc - 32)
                else:
                    newSen += sen[i]
            else:
                newSen += sen[i]

        print(newSen)

fcu = FirstCharUpper()
fcu.upperChar()
