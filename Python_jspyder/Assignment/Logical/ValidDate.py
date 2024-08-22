class Solution:

    def validDate(self, dd, mm, yy):

        if len(str(yy))==4:

            if dd<1 or mm <1 or yy<1:
                print("Invalid Date..")
            elif +2

        else:
            print(f"{yy}->Year is not valid.")