class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        
    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            product.category = self
            
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            product.category = None
            
    def get_total_products(self):
        return len(self.products)