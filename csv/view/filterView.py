import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from fonction.filtrer_attribut_typeF import filter_csv_by_attribute

class FilterView:
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.root)
        self.file_entry = None
        self.attributes_listbox = None
        self.status_label = None
        self.setup_view()
    
    def setup_view(self):
        back_btn = ttk.Button(self.frame, text="Retour", 
                              command=lambda: self.app.show_view("main"))
        back_btn.pack(pady=5)
        
        file_frame = ttk.Frame(self.frame)
        file_frame.pack(pady=10)
        
        file_label = ttk.Label(file_frame, text="Fichier CSV:")
        file_label.pack(side=tk.LEFT)
        
        self.file_entry = ttk.Entry(file_frame)
        self.file_entry.pack(side=tk.LEFT, padx=5)

        self.file_entry.bind("<KeyRelease>", self.check_csv_file)
        
        self.attributes_listbox = tk.Listbox(self.frame, height=5)
        self.attributes_listbox.pack(pady=5)
        
        self.attributes_listbox.bind("<Double-1>", self.on_attribute_double_click)

        self.status_label = ttk.Label(self.frame, text="")
        self.status_label.pack(pady=5)
    
    def check_csv_file(self, event=None):
        if self.file_entry.get().strip().endswith('.csv'):
            self.load_attributes()

    def load_attributes(self):
        try:
            df = pd.read_csv(self.file_entry.get().strip())
            self.attributes_listbox.delete(0, tk.END)
            for col in df.columns:
                self.attributes_listbox.insert(tk.END, col)
            self.status_label.config(text="Attributs chargés avec succès!")
        except Exception as e:
            self.status_label.config(text=f"Erreur: {str(e)}")

    def on_attribute_double_click(self, event):
        try:
            selected = self.attributes_listbox.get(self.attributes_listbox.curselection())

            filter_csv_by_attribute(self.file_entry.get().strip(), selected)
            self.status_label.config(text="Filtrage réussi!")
            
            self.app.root.after(2000, self.app.show_main_view)
            
            script_directory = os.path.dirname(os.path.abspath(__file__))
            filtered_folder = os.path.join(script_directory, "resultat")
            os.startfile(filtered_folder)
        except Exception as e:
            self.status_label.config(text=f"Erreur: {str(e)}")

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
