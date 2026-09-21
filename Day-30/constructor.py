'''class Flipkart:
    products = {'shirts':1000,'handbag':2000,'pants':3000}
    discount = 30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on, grab the products..") 


viswa = Flipkart()
viswa.userinfo('viswa',678912345,'hyd')
viswa.displaydiscount()
viswa.display()
print(viswa.products)
print(viswa.name)


Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)


#using object -> ins,cls,sta,clsatt,insatt
#using class  -> cls,sta,clsatt '''



'''class Flipkart:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        print(f"Hello {self.name}, Welcome to the flipkart")

viswa = Flipkart('viswa',6307892345)
cherry =Flipkart('cherry',6307892345)
ghani = Flipkart('ghani',6307892345) '''



