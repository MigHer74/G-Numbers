from tkinter import Toplevel, LabelFrame, Label, Entry, Radiobutton
from tkinter import IntVar


class GPanel(Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.gameType = IntVar()

        self.build()

    def build(self):
        self.title("G-Numbers | Game Panel")
        self.resizable(False, False)

        self.selectGame = LabelFrame(self, text=" Select Game ")
        self.selectGame.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))

        self.shortSel = Radiobutton(self.selectGame, text="Short Game",
                                    value=1, variable=self.gameType)
        self.shortSel.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.shortLong = Radiobutton(self.selectGame, text="Long Game",
                                     value=2, variable=self.gameType)
        self.shortLong.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.shortPanel = LabelFrame(self, text=" Short Game Numbers ",
                                     labelanchor="n")
        self.shortPanel.grid(row=0, column=1, padx=(15, 15))

        self.shortLabel = Label(self.shortPanel, text="Game #1")
        self.shortLabel.grid(row=0, column=0, padx=(10, 0), pady=10)

        self.shortEntry01 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry01.grid(row=0, column=1, padx=(10, 0), pady=10)

        self.shortEntry02 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry02.grid(row=0, column=2, padx=(10, 0), pady=10)

        self.shortEntry03 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry03.grid(row=0, column=3, padx=(10, 0), pady=10)

        self.shortEntry04 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry04.grid(row=0, column=4, padx=(10, 0), pady=10)

        self.shortEntry05 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry05.grid(row=0, column=5, padx=(10, 0), pady=10)

        self.shortEntry06 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry06.grid(row=0, column=6, padx=(10, 15), pady=10)
