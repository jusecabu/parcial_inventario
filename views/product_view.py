import tkinter as tk
from tkinter import ttk, messagebox
from models.product import Product

class ProductView:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.categories = []
        self.setup_ui()
        
    def setup_ui(self):
        # Form Frame
        form_frame = ttk.LabelFrame(self.frame, text="Registro de Producto", padding=10)
        form_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        # Form Fields
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Descripción:").grid(row=1, column=0, sticky="w")
        self.desc_entry = ttk.Entry(form_frame)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Precio:").grid(row=2, column=0, sticky="w")
        self.price_entry = ttk.Entry(form_frame)
        self.price_entry.grid(row=2, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Stock Inicial:").grid(row=3, column=0, sticky="w")
        self.stock_entry = ttk.Entry(form_frame)
        self.stock_entry.grid(row=3, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Categoría:").grid(row=4, column=0, sticky="w")
        self.category_combo = ttk.Combobox(form_frame, values=[c.name for c in self.categories], state="readonly")
        self.category_combo.grid(row=4, column=1, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Registrar", command=self.register_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_form).pack(side=tk.LEFT, padx=5)
        
        # Product List
        list_frame = ttk.LabelFrame(self.frame, text="Lista de Productos", padding=10)
        list_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        self.tree = ttk.Treeview(list_frame, columns=("Nombre", "Precio", "Stock", "Categoría"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.pack(expand=True, fill="both")

    def update_categories(self, categories):
        self.categories = categories  # Actualizar la lista interna
        self.category_combo['values'] = [c.name for c in self.categories]  # Actualizar opciones
        if self.categories:
            self.category_combo.current(0)
        
    def validate_form(self):
        if not self.name_entry.get().strip() or not self.desc_entry.get().strip() or not self.price_entry.get().strip() or not self.stock_entry.get().strip():
            return False
        try:
            float(self.price_entry.get().strip())
            int(self.stock_entry.get().strip())
        except ValueError:
            return False
        return True
    
    def find_category_by_name(self, name):
        for category in self.categories:  # Asumiendo que tienes una lista de categorías
            if category.name == name:
                return category
        return None

    def add_product_to_tree(self, product):
        self.tree.insert("", "end", values=(product.name, product.price, product.stock, product.category.name if product.category else ""))

    def register_product(self):
        # Validar formulario
        if not self.validate_form() or len(self.categories) < 1:
            return messagebox.showerror("Error", "Todos los campos son obligatorios.")
        
        # Obtener los datos del formulario
        name = self.name_entry.get().strip()
        description = self.desc_entry.get().strip()
        price = float(self.price_entry.get().strip())
        stock = int(self.stock_entry.get().strip())
        category_name = self.category_combo.get().strip()
        
        # Crear una nueva instancia de Product
        category = self.find_category_by_name(category_name)  # Buscar la categoría en la lista de categorías
        new_product = Product(name, description, price, stock, category)
        
        # Añadir el producto al árbol
        self.add_product_to_tree(new_product)
        
        # Limpiar el formulario
        self.clear_form()

        
        messagebox.showinfo("Éxito", "Producto registrado exitosamente.")
        
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.category_combo.current(0)