

class Union:
    def listUnion(self):

        a={1,2,3,4,5,6}
        # inter.--> 2,3,5
        b={3,5,2,9,10}
        c={4,5,3,2,5,8}
        d={9,10,3,2,5,8}
        e={6,7,8,9,10}

        print((a.union(b)).union(c))
        print((a.union(b)).intersection(c))


        print((a.intersection(b)).union(c))

        print((a.intersection(b)).union(c))





        print(())

u=Union()
u.listUnion()