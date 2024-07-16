from tkinter import Toplevel, Frame, LabelFrame, Label, Entry, Button
from tkinter import Radiobutton, IntVar


class GPanel(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()

        self.gameType = IntVar()

        self.build()
        self.focus()

    def build(self):
        self.title("G-Numbers | Game Panel")
        self.resizable(False, False)

        self.panelOne = Frame(self)
        self.panelOne.grid(row=0, column=0, rowspan=2, padx=(15, 10),
                           pady=(15, 15), sticky="n")

        self.selectGame = LabelFrame(self.panelOne, text=" Select Game ")
        self.selectGame.grid(row=0, column=0)

        self.shortSel = Radiobutton(self.selectGame, text="Short Game",
                                    value=1, variable=self.gameType)
        self.shortSel.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.shortLong = Radiobutton(self.selectGame, text="Long Game",
                                     value=2, variable=self.gameType)
        self.shortLong.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.buttonGame = Frame(self.panelOne)
        self.buttonGame.grid(row=1, column=0, pady=(20, 15))

        self.buttonPlay = Button(self.buttonGame, width=15, text="Play Game",
                                 state="disabled")
        self.buttonPlay.grid(row=0, column=0)

        self.buttonReset = Button(self.buttonGame, width=15, text="Reset Game",
                                  state="disabled")
        self.buttonReset.grid(row=1, column=0, pady=(15, 0))

        self.buttonClose = Button(self.buttonGame, width=15, text="Close",
                                  command=self.destroy)
        self.buttonClose.grid(row=2, column=0, pady=(15, 0))

        self.shortPanel = LabelFrame(self, text=" Short Game Numbers ",
                                     labelanchor="n")
        self.shortPanel.grid(row=0, column=1, padx=(15, 15), pady=(15, 0),
                             sticky="n")

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

        self.longPanel = LabelFrame(self, text=" Long Game Numbers ",
                                    labelanchor="n")
        self.longPanel.grid(row=1, column=1, padx=(15, 15), pady=(15, 15))

        self.longLabel1 = Label(self.longPanel, text="Game #1")
        self.longLabel1.grid(row=0, column=0, padx=(10, 0), pady=10)

        self.longEntry11 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry11.grid(row=0, column=1, padx=(10, 0), pady=10)

        self.longEntry12 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry12.grid(row=0, column=2, padx=(10, 0), pady=10)

        self.longEntry13 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry13.grid(row=0, column=3, padx=(10, 0), pady=10)

        self.longEntry14 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry14.grid(row=0, column=4, padx=(10, 0), pady=10)

        self.longEntry15 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry15.grid(row=0, column=5, padx=(10, 0), pady=10)

        self.longEntry16 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry16.grid(row=0, column=6, padx=(10, 15), pady=10)

        self.longLabel2 = Label(self.longPanel, text="Game #2")
        self.longLabel2.grid(row=1, column=0, padx=(10, 0), pady=10)

        self.longEntry21 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry21.grid(row=1, column=1, padx=(10, 0), pady=10)

        self.longEntry22 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry22.grid(row=1, column=2, padx=(10, 0), pady=10)

        self.longEntry23 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry23.grid(row=1, column=3, padx=(10, 0), pady=10)

        self.longEntry24 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry24.grid(row=1, column=4, padx=(10, 0), pady=10)

        self.longEntry25 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry25.grid(row=1, column=5, padx=(10, 0), pady=10)

        self.longEntry26 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry26.grid(row=1, column=6, padx=(10, 15), pady=10)

        self.longLabel3 = Label(self.longPanel, text="Game #3")
        self.longLabel3.grid(row=2, column=0, padx=(10, 0), pady=10)

        self.longEntry31 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry31.grid(row=2, column=1, padx=(10, 0), pady=10)

        self.longEntry32 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry32.grid(row=2, column=2, padx=(10, 0), pady=10)

        self.longEntry33 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry33.grid(row=2, column=3, padx=(10, 0), pady=10)

        self.longEntry34 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry34.grid(row=2, column=4, padx=(10, 0), pady=10)

        self.longEntry35 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry35.grid(row=2, column=5, padx=(10, 0), pady=10)

        self.longEntry36 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry36.grid(row=2, column=6, padx=(10, 15), pady=10)
