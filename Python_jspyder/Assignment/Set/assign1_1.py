
class assign1_1:

    def union(self, first, second):
        first = list(first)
        second = list(second)
        union=[]

        for i in first:
            if i not in union:
                union.append(i)
        for j in second:
            if j not in union:
                union.append(j)
        print(union)


A={1,2,3,4,5,6,7,8}
B={4,6,7,9,10,11,2,4}
a=assign1_1
a.union(A, B)



