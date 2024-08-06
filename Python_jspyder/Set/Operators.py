class Operators:

    def unionS(self):

        A={1,2,3,4,5,6}
        B={7,3,5,8,9,10}


        print(A|B)
        print(A.union())

    def intersectionS(self):
        A = {1, 2, 3, 4, 5, 6}
        B = {7, 3, 5, 8, 9, 10}

        print(A&B)
        print(A.intersection(B))

    def intrUpdate(self):
        A = {1, 2, 3, 4, 5, 6}
        B = {7, 3, 5, 8, 9, 10}

        print(A.intersection(B))
        print(A.intersection_update(B))
        print(A)



    def diffS(self):
        A = {1, 2, 3, 4, 5, 6}
        B = {7, 3, 5, 8, 9, 10}

        print(A - B)
        print(A.difference(B))

    def symmetry(self):
        A = {1, 2, 3, 4, 5, 6}
        B = {7, 3, 5, 8, 9, 10}

        print(A^B)
        print(A.symmetric_difference(B))





u=Operators()


print("Unionv")
u.unionS()

print("intersection")
u.intersectionS()


print("Difference")
u.diffS()

print("symmetry")
u.symmetry()


print("Intersection_Update")
u.intrUpdate()