import tkinter as tk
from tkinter import ttk

class WarehouseView:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.setup_ui()
        
    def setup_ui(self):
        # Form Frame
        form_frame = ttk.LabelFrame(self.frame, text="Registro de Bodega", padding=10)
        form_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        # Form Fields
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Ubicación:").grid(row=1, column=0, sticky="w")
        self.location_entry = ttk.Entry(form_frame)
        self.location_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Capacidad Máxima:").grid(row=2, column=0, sticky="w")
        self.capacity_entry = ttk.Entry(form_frame)
        self.capacity_entry.grid(row=2, column=1, padx=5, pady=2)
        
        # Stock Management
        stock_frame = ttk.LabelFrame(form_frame, text="Gestión de Stock", padding=5)
        stock_frame.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
        
        ttk.Label(stock_frame, text="Producto:").grid(row=0, column=0, sticky="w")
        self.product_combo = ttk.Combobox(stock_frame)
        self.product_combo.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(stock_frame, text="Cantidad:").grid(row=1, column=0, sticky="w")
        self.quantity_entry = ttk.Entry(stock_frame)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(stock_frame, text="Agregar Stock", command=self.add_stock).grid(row=2, column=0, pady=5)
        ttk.Button(stock_frame, text="Retirar Stock", command=self.remove_stock).grid(row=2, column=1, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Registrar", command=self.register_warehouse).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_form).pack(side=tk.LEFT, padx=5)
        
        # Warehouse List
        list_frame = ttk.LabelFrame(self.frame, text="Lista de Bodegas", padding=10)
        list_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        self.tree = ttk.Treeview(list_frame, columns=("Nombre", "Ubicación", "Capacidad", "Ocupación"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Ubicación", text="Ubicación")
        self.tree.heading("Capacidad", text="Capacidad")
        self.tree.heading("Ocupación", text="% Ocupación")
        self.tree.pack(expand=True, fill="both")
        
    def register_warehouse(self):
        # Implementation for registering a warehouse
        pass
        
    def add_stock(self):
        # Implementation for adding stock
        pass
        
    def remove_stock(self):
        # Implementation for removing stock
        pass
        
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.capacity_entry.delete(0, tk.END)
        self.product_combo.set('')
        self.quantity_entry.delete(0, tk.END)