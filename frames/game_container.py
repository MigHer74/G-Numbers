from tkinter import Toplevel, LabelFrame, Radiobutton
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
        self.selectGame.grid(row=0, column=0, padx=15, pady=15)

        self.shortSel = Radiobutton(self.selectGame, text="Short Game",
                                    value=1, variable=self.gameType)
        self.shortSel.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.shortLong = Radiobutton(self.selectGame, text="Long Game",
                                     value=2, variable=self.gameType)
        self.shortLong.grid(row=1, column=0, padx=10, pady=(0, 10))
