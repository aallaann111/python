from tkinter import ttk
import subprocess

class MainView:
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.root)
        self.setup_view()
    
    def setup_view(self):
        label = ttk.Label(self.frame, text="Choisissez un thème :")
        label.pack(pady=10)
        
        btn1 = ttk.Button(self.frame, text="Créer un calendrier", 
                          command=lambda: self.app.show_view("calendrier")) 
        btn1.pack(pady=5)
        
        btn2 = ttk.Button(self.frame, text="Modifier un csv", 
                          command=self.launch_csv_app) 
        btn2.pack(pady=5)
    
    def launch_csv_app(self):
        subprocess.Popen(["python", "csv/app.py"])
        
    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
