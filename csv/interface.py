import tkinter as tk
from tkinter import ttk
from fonction.filtrer_attribut_typeF import filter_csv_by_attribute
import pandas as pd
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélection de fonction CSV")
        self.root.geometry("600x400")
        
        # Créer les vues
        self.main_view = MainView(self)
        self.filter_view = FilterView(self)
        
        # Afficher la vue principale
        self.show_main_view()
    
    def show_main_view(self):
        self.filter_view.hide()
        self.main_view.show()

    def show_filter_view(self):
        self.main_view.hide()
        self.filter_view.show()


class MainView:
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.root)
        self.setup_view()
    
    def setup_view(self):
        label = ttk.Label(self.frame, text="Choisissez une fonction CSV :")
        label.pack(pady=10)
        
        btn1 = ttk.Button(self.frame, text="Filtrer attribut type", 
                          command=self.app.show_filter_view)
        btn1.pack(pady=5)
    
    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()


class FilterView:
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.root)
        self.file_entry = None
        self.attributes_listbox = None
        self.status_label = None
        self.setup_view()
    
    def setup_view(self):
        # Bouton de retour
        back_btn = ttk.Button(self.frame, text="Retour", 
                              command=self.app.show_main_view)
        back_btn.pack(pady=5)
        
        # Cadre pour l'entrée de fichier
        file_frame = ttk.Frame(self.frame)
        file_frame.pack(pady=10)
        
        file_label = ttk.Label(file_frame, text="Fichier CSV:")
        file_label.pack(side=tk.LEFT)
        
        self.file_entry = ttk.Entry(file_frame)
        self.file_entry.pack(side=tk.LEFT, padx=5)

        self.file_entry.bind("<KeyRelease>", self.check_csv_file)
        
        # Liste des attributs
        self.attributes_listbox = tk.Listbox(self.frame, height=5)
        self.attributes_listbox.pack(pady=5)
        
        self.attributes_listbox.bind("<Double-1>", self.on_attribute_double_click)

        # Label de statut
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

            # Exécuter le filtrage
            filter_csv_by_attribute(self.file_entry.get().strip(), selected)
            self.status_label.config(text="Filtrage réussi!")
            
            # Retourner à la vue principale après 2 secondes
            self.app.root.after(2000, self.app.show_main_view)
            
            # Ouvrir le dossier de résultat
            script_directory = os.path.dirname(os.path.abspath(__file__))
            filtered_folder = os.path.join(script_directory, "resultat")
            os.startfile(filtered_folder)
        except Exception as e:
            self.status_label.config(text=f"Erreur: {str(e)}")

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
