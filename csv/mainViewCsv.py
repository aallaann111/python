from tkinter import ttk

class MainViewCsv:
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.root)
        self.setup_view()
    
    def setup_view(self):
        label = ttk.Label(self.frame, text="Choisissez une fonction CSV :")
        label.pack(pady=10)
        
        btn1 = ttk.Button(self.frame, text="Filtrer attribut type", 
                          command=lambda: self.app.show_view("filter")) 
        btn1.pack(pady=5)

        btn2 = ttk.Button(self.frame, text="Traitement des colonnes", 
                          command=lambda: self.app.show_view("process")) 
        btn2.pack(pady=5)
        
        btn3 = ttk.Button(self.frame, text="Refactoriser fichier", 
                          command=lambda: self.app.show_view("refactor"))
        btn3.pack(pady=5)
        
    
    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()