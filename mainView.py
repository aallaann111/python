from tkinter import ttk

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

        #btn2 = ttk.Button(self.frame, text="Traitement des colonnes", 
        #                  command=lambda: self.app.show_view("process")) 
        #btn2.pack(pady=5)
    
    
    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
