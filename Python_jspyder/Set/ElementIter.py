

class SetEle:

    def eleSet(self):

        s={"Apple", "Papay", "Mango"}

        length=len(s)

        for i in s:
            print(i)

        print("********** Using while loop **************")
        while (length!=0):
            se=list(s)

            print(se)
            length-=1




e=SetEle()
e.eleSet()

