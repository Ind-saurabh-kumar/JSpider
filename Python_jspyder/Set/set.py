
a = {10, 20, 30, 40, 50}
class Set:


    # set Creation
    def create(self):
        a={10, 20, 30, 40, 50}
        print(a)

    # duplicate values
        b= {10, 20, 30, 40, 50, 10}
        print(f"b={b}")

    def emptySetcreate(self):
        c=set()

        print(c)

    def addEle(self):
        c=set()
        c.add(10)
        c.add(30)
        c.add(40)
        c.add(95)
        c.add(75)
        c.add(50)
        print(c)

    def hetrogEle(self):
        d={50, 40, "john", 'a', 56.76}
        print(d)


    def popEle(self):
        r=a.pop()
        print(r)
        r=a.pop()
        print(r)

    def removeEle(self):
        print(f"Before removing an elements\n a={a}")
        dele = a.remove(20)
        print(dele)
        print(a)











s=Set()
s.create()
s.emptySetcreate()
s.addEle()
s.hetrogEle()

s.popEle()

s.removeEle()
