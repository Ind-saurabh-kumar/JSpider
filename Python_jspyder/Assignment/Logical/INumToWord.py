class InumToWord:

    def number(self, n):

        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen' 'Nineteen']

        tens = ['', '', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


        if n < 20:
            return (ones[n])
        elif n < 100:
            return (tens[n // 10] + " " + ones[n % 10])

        elif n < 1000:
            return (ones[n // 100] + " Hundred " + self.number(n % 100))

        elif n < 10000:
            return (ones[n // 1000] + " Thousand " + self.number(n % 1000))

        elif n < 100000:
            return (self.number(n // 1000) + " Thousand " + self.number(n % 1000))

        elif n < 1000000:
            r=n//1000
            nr=n%1000
            print(nr)
            return (ones[r//100]+ " Hundred " + self.number(n//1000)+ " Thousand " + self.number(n % 10000))

        # elif n < 1000000:
        #     return (self.number(n // 100000) + " Lakh " + self.number(n % 100000))
        # elif n < 10000000:
        #     return (self.number(n // 100000) + " Lakh " + self.number(n % 100000))
        #
        # elif n < 100000000:
        #     return (ones[n // 10000000] + " Crore " + self.number(n % 10000000))
        #
        # elif n < 1000000000:
        #     return (self.number(n // 10000000) + " Crore " + self.number(n % 10000000))
        #
        # elif n < 10000000000:
        #     return (ones[n // 1000000000] + " Hundred " + self.number(n % 1000000000))

        else:
            return "Give positive number only upto hundreds of crore"


s=InumToWord()
print(s.number(123000))