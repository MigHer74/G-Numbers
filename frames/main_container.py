from tkinter import Tk, Menu


class Gnumber(Tk):
    def __init__(self):
        super().__init__()
        self.build()
        self.menu()

    def build(self):
        self.title("G-Numbers - Main Menu")
        self.geometry("600x400")

    def menu(self):
        self.mainMenu = Menu()

        self.optionGame = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Game", menu=self.optionGame)

        self.optionGame.add_command(label="Play")
        self.optionGame.add_command(label="RePlay")
        self.optionGame.add_separator()
        self.optionGame.add_command(label="Exit", command=self.quit)

        self.optionView = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="View", menu=self.optionView)

        self.optionView.add_cascade(label="Short Game")
        self.optionView.add_cascade(label="Long Game")

        self.optionData = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Data", menu=self.optionData)

        self.optionData.add_cascade(label="Previous Data")
        self.optionData.add_cascade(label="Winner Numbers")

        self.optionAbout = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="About", menu=self.optionAbout)

        self.config(menu=self.mainMenu)
