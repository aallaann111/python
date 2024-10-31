import tkinter as tk
from tkinter import ttk
from fonction.filtrer_attribut_typeF import filter_csv_by_attribute
from fonction.suppression_colonneF import process_csv_columns
import pandas as pd
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélection de fonction CSV")
        self.root.geometry("600x400")
        
        self.main_frame = ttk.Frame(root)
        self.filter_frame = ttk.Frame(root)
        #self.process_frame = ttk.Frame(root)
        
        self.setup_main_view()
        self.setup_filter_view()
        #self.setup_process_view()
        
        self.show_main_view()
    
    def setup_main_view(self):
        label = ttk.Label(self.main_frame, text="Choisissez une fonction CSV :")
        label.pack(pady=10)
        
        btn1 = ttk.Button(self.main_frame, text="Filtrer attribut type", 
                         command=self.show_filter_view)
        btn1.pack(pady=5)
    
    def setup_filter_view(self):
        back_btn = ttk.Button(self.filter_frame, text="Retour", 
                              command=self.show_main_view)
        back_btn.pack(pady=5)
        
        file_frame = ttk.Frame(self.filter_frame)
        file_frame.pack(pady=10)
        
        file_label = ttk.Label(file_frame, text="Fichier CSV:")
        file_label.pack(side=tk.LEFT)
        
        self.file_entry = ttk.Entry(file_frame)
        self.file_entry.pack(side=tk.LEFT, padx=5)

        self.file_entry.bind("<KeyRelease>", self.check_csv_file)
        
        self.attributes_listbox = tk.Listbox(self.filter_frame, height=5)
        self.attributes_listbox.pack(pady=5)
        
        self.attributes_listbox.bind("<Double-1>", self.on_attribute_double_click)

        self.status_label = ttk.Label(self.filter_frame, text="")
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
            
            self.root.after(2000, self.show_main_view)
            
            script_directory = os.path.dirname(os.path.abspath(__file__))
            filtered_folder = os.path.join(script_directory, "resultat")
            os.startfile(filtered_folder)
        except Exception as e:
            self.status_label.config(text=f"Erreur: {str(e)}")

    def show_main_view(self):
        self.filter_frame.pack_forget()
        self.main_frame.pack()
    
    def show_filter_view(self):
        self.main_frame.pack_forget()
        self.filter_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
