
class Dictionary:

    def createDict(self):

        studentInfo={'sID':101, 'sName':'Saurabh Kumar', 'sNumber':1234568791 }

        print(type(studentInfo))
        print(studentInfo)

        print(" ********* Second method to create dict.  ********* ")
        fruit={}
        fruit[1]='Apple'
        fruit[2]='Banana'
        print(fruit)

        print("***** Fetching data using get method in dict **** ")
        print(fruit.get(3))
        print(fruit.get(2 ))

    def retriveData(self):
        print(" ********* Fetching Data from dict.  ********* ")
        sampleDict={1:'Apple', 2: 'Banana', 3: 'CustardApple'}
        print(sampleDict[2])


    def enterData(self):
        print(" ********* Entering Data from dict.  ********* ")
        studentRecord={}

        numberStudent=int(input("Enter the number of student:- \n"))

        i=0
        while i<numberStudent:

            rollNumber= int(input("Enter the roll number \n"))
            percentage = input ("Enter the percentage \n")

            studentRecord[rollNumber]=percentage

            i=i+1
        print(studentRecord)






c=Dictionary()
c.createDict()

c.retriveData()

c.enterData()