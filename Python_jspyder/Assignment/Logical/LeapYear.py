
class LeapYear:

    def leapY(self):
        year=int(input("Enter the Year: \n"))

        if (year%100 != 0 or year%400 == 0) and year % 4==0:
            print(f"{year} is Leap year.")

        else:
            print(f"{year} is not Leap year.")

ly=LeapYear()
ly.leapY()