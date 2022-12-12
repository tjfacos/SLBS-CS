class Product:

    def __init__(self, description, price, inventory) -> None:
        self.__description= description
        self.__inventory = inventory
        self.__price = price

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

    def __str__(self) -> str:
        return f"{self.__description} £{self.__price} Inventory: {self.__inventory}" 

    def display(self):
        
        print(f"""

        Description: {self.get_description()}
        Price:       £{self.get_price()}
        Inventory:   {self.get_inventory()}

        """)        

prod3 = Product("parsnip", 0.5, 12)
prod4 = Product("cucumber", 0.75, 16)

print(prod3)
print(prod4)