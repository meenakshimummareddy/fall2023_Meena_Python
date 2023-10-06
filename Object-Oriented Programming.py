# Define Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Define Customer class
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Define Order class with inheritance
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

# Create instances of classes
product1 = Product("Laptop", 999)
customer1 = Customer("John", "john@example.com")
order1 = Order(customer1)
order1.add_product(product1)

# Example usage
print(f"Customer: {order1.customer.name}")
print("Products in the order:")
for product in order1.products:
    print(f"{product.name}: ${product.price}")
