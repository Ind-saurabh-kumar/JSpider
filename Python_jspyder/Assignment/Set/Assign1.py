

class Assign:

    def union(self,first, second):
        resUnion=first|second
        # print(f"Union of A and  B is {resUnion}")
        return resUnion

    def intersection(self, first,second):
        resInter=first&second
        # print(f"Union of A and  B is {resInter}")
        return resInter

    def difference(self, first,second):
        resDeff=first-second
        # print(f"Union of A and  B is {resDeff}")
        return resDeff


A={1,2,3,4,5,6}
B={1,2,3,8,9,10,11}
C={1,2,3,6,12,15,18}
a=Assign()

# ***** question 1 ***************
print("******** Question 1 **************** ")
buc=B|C   # B union C
anbuc=buc&A   # A intersection (B union C)
print(f" A inetersection (B union C) is ={anbuc}")

# ********* question 2 ****************
print("******** Question 2 **************** ")
bdc = B-C    # B diff C
aubdc = A|bdc   # A union B diff C
print(f" A union (B diff C) is ={aubdc}")




