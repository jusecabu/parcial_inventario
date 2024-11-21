import tkinter as tk
from tkinter import ttk
from models.category import Category

class CategoryView:
    def __init__(self, parent, product_view=None):
        self.frame = ttk.Frame(parent)
        self.product_view = product_view
        self.categories = []
        self.setup_ui()
        
    def setup_ui(self):
        # Form Frame
        form_frame = ttk.LabelFrame(self.frame, text="Registro de Categoría", padding=10)
        form_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        # Form Fields
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Descripción:").grid(row=1, column=0, sticky="w")
        self.desc_entry = ttk.Entry(form_frame)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Registrar", command=self.register_category).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_form).pack(side=tk.LEFT, padx=5)
        
        # Category List
        list_frame = ttk.LabelFrame(self.frame, text="Lista de Categorías", padding=10)
        list_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        self.tree = ttk.Treeview(list_frame, columns=("Nombre", "Descripción", "Productos"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Productos", text="# Productos")
        self.tree.pack(expand=True, fill="both")

    def add_category_to_tree(self, category):
        self.tree.insert("", "end", values=(category.name, category.description, category.get_total_products()))

    def validate_form(self):
        if not self.name_entry.get().strip() or not self.desc_entry.get().strip():
            return False
        return True

    def get_all_categories(self):
        return [category for category in self.categories]

    def register_category(self):
        # Validar formulario
        if not self.validate_form():
            return tk.messagebox.showerror("Error", "Todos los campos son obligatorios.")
        
        # Crear instancia de Category
        name = self.name_entry.get().strip()
        description = self.desc_entry.get().strip()
        new_category = Category(name, description)
        
        # Añadir la categoría al árbol
        self.add_category_to_tree(new_category)
        self.categories.append(new_category)
        
        if self.product_view:
            self.product_view.update_categories(self.get_all_categories())  # Actualizar el combobox
        

        # Limpiar formulario
        self.clear_form()
        
        tk.messagebox.showinfo("Éxito", "Categoría registrada exitosamente.")
        
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)