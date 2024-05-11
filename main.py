class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    # Call get_price method
    def get_price(self, num_of_items):
        # Regular charge less for orders of less than 10 items
        if num_of_items < 10:
            cost = num_of_items * self.price
        # 10% discount for orders of between 10 and 99 items
        elif 10 <= num_of_items <= 99:
            cost = num_of_items * self.price * 0.9
        # 20% discount for orders of 100 or more items
        else:
            cost = num_of_items * self.price * 0.8
        return cost

    # Call make_purchase method
    def make_purchase(self, num_of_items):
        self.amount -= num_of_items

# Prompt user input
name = input('Enter the product name: ')
amount = input('Enter the product amount: ')
price = input('Enter the product price: ')

# Create product instance
product = Product(name, amount, price)
print(f'The {product.name} is currently in stock with {product.amount}'
      f' units at a price of ${product.price} each.')


