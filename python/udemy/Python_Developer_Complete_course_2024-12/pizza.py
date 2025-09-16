# name, price, ingredients, vegeterian

class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"pizza {self.name}: {self.price}$")


# pizza1 = Pizza()
# pizza1.name = "4 cheeses"
# pizza1.price = 8.99

# print(pizza1)
# print(pizza1.name, pizza1.price)
# pizza1.display()

pizza1 = Pizza("4 cheeses", 8.99)
pizza1.display()