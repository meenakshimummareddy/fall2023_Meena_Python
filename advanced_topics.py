# Dictionary example
phone_book = {
    'Alice': '1234',
    'Bob': '5678',
    'Charlie': '9012'
}

# Set example
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Tuple example
person = ('John', 30, 'john@example.com')


# Custom Objects example
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


car1 = Car('Toyota', 'Corolla', 2022)
car2 = Car('Tesla', 'Model S', 2023)

print(phone_book)
print(set1.union(set2))
print(person)
print(car1.display_info())
print(car2.display_info())
