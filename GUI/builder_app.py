from ..horloge.Horloge import Horloge
from threading import Thread
import tkinter as tk
from tkinter import ttk


class BuilderApp(Thread):
    def __init__(self,horloge:Horloge):
        super().__init__()
        self.root = tk.Tk()

        
        pass

    def build_and_run(self):
        entry = ttk.Entry(self.root, width=20)
        entry.pack()
        self.root.mainloop()
        pass

    def run(self):
        self.build_and_run()
        pass