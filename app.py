# app.py

"""
Main application module that initializes and manages different views using tkinter.
"""

import tkinter as tk
from calendrier.calendrier_View import CalendrierView
from Main_View import MainView


class App:
    """
    Main application class that initializes the application window and manages different views.
    """

    def __init__(self, root):
        """Initialize the application with the main tkinter window."""
        self.root = root
        self.root.title("Application")
        self.root.geometry("600x400")
        
        self.views = {
            "main": MainView(self),
            "calendrier": CalendrierView(self)
        }
        
        self.show_view("main")
        
    def show_view(self, view_name):
        """Hide all views except the specified view."""
        for _, view in self.views.items():
            view.hide()
        
        self.views[view_name].show()


if __name__ == "__main__":
    main_root = tk.Tk()
    app = App(main_root)
    main_root.mainloop()
