#
#
# num=170
#
# print(num.__hash__())
#
# print("Saurabh".__hash__())
#
# print((1,).__hash__())


class User:

    def __init__(self, name, occupation):

        self.name= name
        self.occupation = occupation


u1=User("Saurabh", "Student")

u2=User("Saurabh", "Student")


print(u1.name, u1.occupation)
print(u2)


#  Print the hash of user1 u1

print('hash of user1 \n', hash(u1) )

print("has of user 1 \n", hash(u2))

# Check u1 and u2 is equal or not

if u1==u2:
    print("User is same")
else:
    print("User is different")