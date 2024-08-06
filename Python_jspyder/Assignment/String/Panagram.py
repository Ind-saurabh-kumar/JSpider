

class PanagramStr:

    def strPanagram(self):

        string=input("Enter your String \n")
        azStr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        string=string.upper()
        match=True

        for char in azStr:
            if char not in string:
                match=False
        if match==True:
            print("Panagram")
        else:
            print("Not Panagram")


p=PanagramStr()
p.strPanagram()
