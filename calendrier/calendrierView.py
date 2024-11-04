import tkinter as tk
from tkinter import ttk
from datetime import datetime

from calendrier.calendrierPrevi import calendrierPrevisionnel


class calendrierView:
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.root)
        self.entries = []
        self.phases = {}
        self.setup_view()

    def setup_view(self):
        back_btn = ttk.Button(self.frame, text="Retour", 
                              command=lambda: self.app.show_view("main"))
        back_btn.pack(pady=5)

        self.entries_frame = ttk.LabelFrame(self.frame, text="Phases du projet")
        self.entries_frame.pack(pady=10, fill="both", expand=True)

        add_row_btn = ttk.Button(self.frame, text="Ajouter une Phase", command=self.add_row)
        add_row_btn.pack(pady=5)

        save_btn = ttk.Button(self.frame, text="Sauvegarder et Exécuter", command=self.save_and_execute)
        save_btn.pack(pady=5)
        
        self.status_label = ttk.Label(self.frame, text="")
        self.status_label.pack(pady=5)

    def add_row(self):
        row_frame = ttk.Frame(self.entries_frame)
        row_frame.pack(fill="x", padx=5, pady=2)

        title_label = ttk.Label(row_frame, text="Intitulé:")
        title_label.pack(side=tk.LEFT)
        title_entry = ttk.Entry(row_frame)
        title_entry.pack(side=tk.LEFT, padx=5)

        start_label = ttk.Label(row_frame, text="Date Début (YYYY-MM-DD):")
        start_label.pack(side=tk.LEFT)
        start_entry = ttk.Entry(row_frame)
        start_entry.pack(side=tk.LEFT, padx=5)

        end_label = ttk.Label(row_frame, text="Date Fin (YYYY-MM-DD):")
        end_label.pack(side=tk.LEFT)
        end_entry = ttk.Entry(row_frame)
        end_entry.pack(side=tk.LEFT, padx=5)

        self.entries.append((title_entry, start_entry, end_entry))

    def save_and_execute(self):
        self.phases.clear()

        try:
            for title_entry, start_entry, end_entry in self.entries:
                title = title_entry.get().strip()
                start_date = start_entry.get().strip()
                end_date = end_entry.get().strip()

                if not title or not start_date or not end_date:
                    self.status_label.config(text=f"Erreur : Tous les champs doivent être remplis pour chaque phase.")
                    return

                start_dt = datetime.strptime(start_date, "%Y-%m-%d")
                end_dt = datetime.strptime(end_date, "%Y-%m-%d")
                if start_dt > end_dt:
                    self.status_label.config(text=f"Erreur: La date de début pour '{title}' est postérieure à la date de fin.")
                    return

                self.phases[title] = (start_date, end_date)

            calendrierPrevisionnel.plot_project_timeline(self.phases)

            self.status_label.config(text=f"Succès : Phases sauvegardées et visualisées avec succès.")
            
            self.app.show_view("main")

        except ValueError as e:
            self.status_label.config(text=f"Erreur: {str(e)}")

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()