class Product:

    def __init__(self):
        self.__name=None
        self.__price=None
        self.__qnt_In_Stock=None
        self.__upd_stock_Qnt=None


    def setName(self, pName):
        self.__name=pName

    def setPrice(self, pPrice):
        self.__price=pPrice


    def setQnt(self, qnt):
        self.__qnt_In_Stock=qnt

    def setupdQnt(self, uQnt):
        self.__upd_stock_Qnt=uQnt


    def getPName(self):
        return self.__name

    def getPPrice(self):
        return self.__price

    def getPQnt(self):
        return self.__qnt_In_Stock

    def getInfo(self):
        return (f"Product_Name: {self.__name} \n"
                f"Price: {self.__price}\n"
                f"Quantity: {self.__qnt_In_Stock}\n")


class Order(Product):
    def __init__(self):
        self.orderId="ORD"+str( )



    def getProduct(self):
        return self.product








p=Product()
p.setName("Product1")
p.setPrice(10000.00)
p.setQnt(10)

print(p.getInfo())

p2=Product()
p2.setName("Product2")
p2.setPrice(12000.0)
p2.setQnt(101)
print(p2.getInfo())

print("Product ")
o=Order()
print(o.getProduct())
