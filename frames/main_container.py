from tkinter import Tk, Menu, LabelFrame, Label, Entry


class Gnumber(Tk):
    def __init__(self):
        super().__init__()
        self.build()
        self.menu()

    def build(self):
        self.title("G-Numbers - Main Menu")
        self.geometry("600x400")

        self.titlePanel = LabelFrame(self)
        self.titlePanel.pack()

        self.titleLabel = Label(self.titlePanel, text="Latest Results")
        self.titleLabel.grid(row=0, column=0)

        self.shortPanel = LabelFrame(self, text=" Short Game Results")
        self.shortPanel.pack()

        self.shortLabel = Label(self.shortPanel, text="Game #1")
        self.shortLabel.grid(row=0, column=0)

        self.shortEntry1 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry1.grid(row=0, column=1)

        self.shortEntry2 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry2.grid(row=0, column=2)

        self.shortEntry3 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry3.grid(row=0, column=3)

        self.shortEntry4 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry4.grid(row=0, column=4)

        self.shortEntry5 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry5.grid(row=0, column=5)

        self.shortEntry6 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry6.grid(row=0, column=6)

        self.longPanel = LabelFrame(self, text=" Long Game Results")
        self.longPanel.pack()

        self.longLabel1 = Label(self.longPanel, text="Game #1")
        self.longLabel1.grid(row=0, column=0)

        self.longEntry11 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry11.grid(row=0, column=1)

        self.longEntry12 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry12.grid(row=0, column=2)

        self.longEntry13 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry13.grid(row=0, column=3)

        self.longEntry14 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry14.grid(row=0, column=4)

        self.longEntry15 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry15.grid(row=0, column=5)

        self.longEntry16 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry16.grid(row=0, column=6)

        self.longLabel2 = Label(self.longPanel, text="Game #2")
        self.longLabel2.grid(row=1, column=0)

        self.longEntry21 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry21.grid(row=1, column=1)

        self.longEntry22 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry22.grid(row=1, column=2)

        self.longEntry23 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry23.grid(row=1, column=3)

        self.longEntry24 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry24.grid(row=1, column=4)

        self.longEntry25 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry25.grid(row=1, column=5)

        self.longEntry26 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry26.grid(row=1, column=6)

        self.longLabel3 = Label(self.longPanel, text="Game #3")
        self.longLabel3.grid(row=2, column=0)

        self.longEntry31 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry31.grid(row=2, column=1)

        self.longEntry32 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry32.grid(row=2, column=2)

        self.longEntry33 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry33.grid(row=2, column=3)

        self.longEntry34 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry34.grid(row=2, column=4)

        self.longEntry35 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry35.grid(row=2, column=5)

        self.longEntry36 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry36.grid(row=2, column=6)

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
