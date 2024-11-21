import tkinter as tk
from tkinter import ttk, messagebox
from views.product_view import ProductView
from views.category_view import CategoryView
from views.supplier_view import SupplierView
from views.warehouse_view import WarehouseView
from views.reports_view import ReportsView

class InventoryManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Inventarios")
        self.root.geometry("1200x700")
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Initialize views
        self.supplier_view = SupplierView(self.notebook)
        self.product_view = ProductView(self.notebook, self.supplier_view)
        self.category_view = CategoryView(self.notebook, self.product_view)
        self.warehouse_view = WarehouseView(self.notebook)
        self.reports_view = ReportsView(self.notebook)
        
        # Add tabs
        self.notebook.add(self.product_view.frame, text="Productos")
        self.notebook.add(self.category_view.frame, text="Categorías")
        self.notebook.add(self.supplier_view.frame, text="Proveedores")
        self.notebook.add(self.warehouse_view.frame, text="Bodegas")
        self.notebook.add(self.reports_view.frame, text="Reportes")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = InventoryManagementSystem()
    app.run()