import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from fonction.suppression_colonneF import process_csv_columns

class SuppressionColonneView:
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.root)
        self.file_entry = None
        self.columns_action_vars = {} 
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
        
        self.columns_frame = ttk.LabelFrame(self.frame, text="Colonnes à traiter")
        self.columns_frame.pack(pady=10, fill="both", expand=True)
        
        process_btn = ttk.Button(self.frame, text="Filtrer", command=self.process_columns)
        process_btn.pack(pady=10)
        
        self.status_label = ttk.Label(self.frame, text="")
        self.status_label.pack(pady=5)

    def check_csv_file(self, event=None):
        file_path = self.file_entry.get().strip()
        if file_path.endswith('.csv'):
            self.load_columns()

    def load_columns(self):
        try:
            file_path = self.file_entry.get().strip()
            if not os.path.exists(file_path) or not file_path.endswith('.csv'):
                self.status_label.config(text="Erreur : Fichier CSV non valide.")
                return
            
            df = pd.read_csv(file_path)
            for widget in self.columns_frame.winfo_children():
                widget.destroy()
            
            self.columns_action_vars = {}
            
            for col in df.columns:
                frame = ttk.Frame(self.columns_frame)
                frame.pack(fill="x", padx=5, pady=2)
                
                label = ttk.Label(frame, text=col)
                label.pack(side=tk.LEFT)
                
                action_var = tk.StringVar(value="none")
                none_radio = ttk.Radiobutton(frame, text="Aucun", variable=action_var, value="none")
                none_radio.pack(side=tk.LEFT, padx=5)
                
                content_radio = ttk.Radiobutton(frame, text="Contenu", variable=action_var, value="contenu")
                content_radio.pack(side=tk.LEFT, padx=5)
                
                column_radio = ttk.Radiobutton(frame, text="Colonne", variable=action_var, value="colonne")
                column_radio.pack(side=tk.LEFT, padx=5)
                
                self.columns_action_vars[col] = action_var
            
            self.status_label.config(text="Colonnes chargées avec succès!")
        except Exception as e:
            self.status_label.config(text=f"Erreur: {str(e)}")

    def process_columns(self):
        try:
            file_path = self.file_entry.get().strip()
            columns_to_process = []
            actions = []
            
            for column, action_var in self.columns_action_vars.items():
                action = action_var.get()
                if action in ["contenu", "colonne"]:
                    columns_to_process.append(column)
                    actions.append(action)

            result_file = process_csv_columns(file_path, columns_to_process, actions)
            if result_file:
                self.status_label.config(text="Filtrage réussi!")
                
                self.app.root.after(2000, lambda: self.app.show_view("main"))
                
                script_directory = os.path.dirname(os.path.abspath(__file__))
                filtered_folder = os.path.join(script_directory, "resultat")
                os.startfile(filtered_folder)
            else:
                self.status_label.config(text="Erreur lors du traitement des colonnes.")
        except Exception as e:
            self.status_label.config(text=f"Erreur: {str(e)}")

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
