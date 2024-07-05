from tkinter import Tk


class Gnumber(Tk):
    def __init__(self):
        super().__init__()
        self.build()

    def build(self):
        self.title("G-Numbers - Main Menu")
        self.geometry("600x400")
