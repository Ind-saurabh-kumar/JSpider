
t=(1,2,3,4,5,6)
print(type(t))

print(min(t))

print(max(t))

print(len(t))

print(t.count(6))

print(t.index(4))

a=10
b=20
c=30
d=40
e=50
f=60
pack=a,b,c,d,e,f
print(pack)

unpack=1,2,3,4,56,45
x,y,z,r,t,i=unpack
print(x)
print(y)
print(z)
print(r)
print(t)
print(i)


# class TupleInbuiltMethod:
#
#     def display(self):
#         print(t)
#
#     def length(self):
#         print(len(t))
#
#     def pindex(self):
#         print("******* tuple positive indexing *************")
#         for i in range(1, len(t)+1):
#             print(t.index(i))
#
#
#
#     def nindex(self):
#
#         print("******** Negative Indexing *******")
#         l=len(t)
#         while(l>=1):
#             print(t.index())
#             l=l-1;
#
#
#
# tu=TupleInbuiltMethod()
# tu.pindex()
#
#
#
# # /4Ype3E
# tu.nindex()