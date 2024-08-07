class SubList:

    def finSubList(self):
        l=[1,2,3,4,5,6,7,8,9]
        sl=[]
        flag=False

        for i in sl:
                if i in l:
                    flag=True
                else:
                    flag=False

        if flag==True:
            print(f"{sl} is the sublist of {l}")
        else:
            print(f"{sl} is not the sublist of {l}")

sl=SubList()
sl.finSubList()


