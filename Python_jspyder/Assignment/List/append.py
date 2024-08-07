

class Adding:

    def eleAdd(self):
        l=[1,3,5,3,2,6]
        # pos=int(input("Enter the position \n"))
        val=int(input("Enter the value \n"))

        nl=[]

        ins=False

        for value in l:
            if not ins and value<=val:
                nl.append(val)
                ins=True;
            nl.append(val)

        if not ins:
            nl.append(val)

        print(nl)


i=Adding()
i.eleAdd()