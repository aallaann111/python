import tkinter as tk
from calendrier.calendrierView import calendrierView
from mainView import MainView


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Application")
        self.root.geometry("600x400")
        
        self.views = {
            "main": MainView(self),
            "calendrier": calendrierView(self)
        }
        
        self.show_view("main")
        
    def show_view(self, view_name):
        for name, view in self.views.items():
            view.hide()
        
        self.views[view_name].show()
    
    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()