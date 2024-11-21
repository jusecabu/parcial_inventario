class Warehouse:
    def __init__(self, name, location, max_capacity):
        self.name = name
        self.location = location
        self.max_capacity = max_capacity
        self.products = {}  # Dictionary to store product: quantity pairs
        
    def add_product(self, product, quantity):
        current_total = sum(self.products.values())
        if current_total + quantity <= self.max_capacity:
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity
            return True
        return False
        
    def remove_product(self, product, quantity):
        if product in self.products:
            if self.products[product] >= quantity:
                self.products[product] -= quantity
                if self.products[product] == 0:
                    del self.products[product]
                return True
        return False
        
    def get_product_quantity(self, product):
        return self.products.get(product, 0)
        
    def get_available_capacity(self):
        return self.max_capacity - sum(self.products.values())