import tkinter as tk
from tkinter import ttk

class SupplierView:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.setup_ui()
        
    def setup_ui(self):
        # Form Frame
        form_frame = ttk.LabelFrame(self.frame, text="Registro de Proveedor", padding=10)
        form_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        # Form Fields
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Dirección:").grid(row=1, column=0, sticky="w")
        self.address_entry = ttk.Entry(form_frame)
        self.address_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Teléfono:").grid(row=2, column=0, sticky="w")
        self.phone_entry = ttk.Entry(form_frame)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=2)
        
        # Product Assignment
        ttk.Label(form_frame, text="Productos:").grid(row=3, column=0, sticky="w")
        self.products_listbox = tk.Listbox(form_frame, selectmode=tk.MULTIPLE)
        self.products_listbox.grid(row=3, column=1, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Registrar", command=self.register_supplier).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_form).pack(side=tk.LEFT, padx=5)
        
        # Supplier List
        list_frame = ttk.LabelFrame(self.frame, text="Lista de Proveedores", padding=10)
        list_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        self.tree = ttk.Treeview(list_frame, columns=("Nombre", "Dirección", "Teléfono", "Productos"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Productos", text="# Productos")
        self.tree.pack(expand=True, fill="both")
        
    def register_supplier(self):
        # Implementation for registering a supplier
        pass
        
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.products_listbox.selection_clear(0, tk.END)