# We want to build an online shopping cart system that allows users to add products to their cart, calculate the total cost, apply discounts, and generate an invoice. The system should include the following functionalities:

# Adding products to the cart
# Removing products from the cart
# Calculating the total cost
# Applying discounts based on user type
# Generating an invoice


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, name, is_premium=False):
        self.name = name
        self.is_premium = is_premium


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total_cost(self):
        total = sum(product.price for product in self.products)

        if self.user.is_premium:
            total *= 0.9
        return total

user1 = User("Sanjeev ",is_premium=True)

p1 = Product("Laptop",10000000)
p2 = Product("Mouse",1000)

cart = ShoppingCart(user1)


cart.add_product(p1)
cart.add_product(p2)

print("Total Cost : ",cart.calculate_total_cost())
