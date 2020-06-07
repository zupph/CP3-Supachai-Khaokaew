class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to", self.name, self.lastName, "'s cart")

customer1 = Customer()
customer1.name = "Somchai"
customer1.lastName = "Jaochan"
customer1.age = 50
customer1.addCart()

customer2 = Customer()
customer2.name = "Sompong"
customer2.lastName = "Kkanyuraphe"
customer2.age = 49
customer2.addCart()

customer3 = Customer()
customer3.name = "Sommai"
customer3.lastName = "Yungbamru"
customer3.age = 48
customer3.addCart()

customer4 = Customer()
customer4.name = "Somsak"
customer4.lastName = "Chunweerakarn"
customer4.age = 47
customer4.addCart()
