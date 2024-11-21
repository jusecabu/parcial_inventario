class Product:
    def __init__(self, name, description, price, initial_stock, category=None):
        self.name = name
        self.description = description
        self.price = price
        self.stock = initial_stock
        self.category = category
        self.suppliers = []
        
    def add_stock(self, quantity):
        self.stock += quantity
        
    def remove_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
    
    def get_total_value(self):
        return self.price * self.stock
    
    def add_supplier(self, supplier):
        if supplier not in self.suppliers:
            self.suppliers.append(supplier)
            
    def remove_supplier(self, supplier):
        if supplier in self.suppliers:
            self.suppliers.remove(supplier)