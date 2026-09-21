class Flipkart:
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


cherry = Flipkart()
cherry.userinfo('cherry',678912345,'vizag')
cherry.displaydiscount()
cherry.display()


ghani = Flipkart()
ghani.userinfo('ghani',678912345,'che')
ghani.displaydiscount()
ghani.display()


