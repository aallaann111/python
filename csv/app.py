import tkinter as tk
from mainViewCsv import MainViewCsv
from view.filterView import FilterView
from view.SuppressionColonneView import SuppressionColonneView
#from view.refactorFileView import RefactorFileView


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélection de fonction CSV")
        self.root.geometry("600x400")
        
        self.views = {
            "main": MainViewCsv(self),
            "filter": FilterView(self),
            "process": SuppressionColonneView(self),
            #"refactor": RefactorFileView(self),
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