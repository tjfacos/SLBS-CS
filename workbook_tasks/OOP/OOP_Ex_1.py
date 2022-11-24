class Product:
        
    def set_description(self, desc):
        self.__description = desc

    def get_description(self):
        return self.__description

    def set_price(self, p):
        self.__price = p

    def get_price(self):
        return self.__price
    
    def set_inventory(self, inventory):
        self.__inventory = inventory

    def get_inventory(self):
        return self.__inventory

prod2 = Product()
prod2.set_description("chocolate bar")
prod2.set_price(1.5)
prod2.set_inventory(24) 

print(f"""

Description: {prod2.get_description()}
Price:       £{prod2.get_price()}
Inventory:   {prod2.get_inventory()}
""")