from tkinter import Toplevel, Frame, LabelFrame, Label, Entry, Button
from tkinter import Radiobutton, StringVar


class GPanel(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()

        self.gameType = StringVar()
        self.gameType.set(None)

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
                                    value="short", variable=self.gameType,
                                    command=self.gameAction)
        self.shortSel.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.longSel = Radiobutton(self.selectGame, text="Long Game",
                                   value="long", variable=self.gameType,
                                   command=self.gameAction)
        self.longSel.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.buttonGame = Frame(self.panelOne)
        self.buttonGame.grid(row=1, column=0, pady=(20, 15))

        self.buttonPlay = Button(self.buttonGame, width=15, text="Play Game",
                                 state="disabled")
        self.buttonPlay.grid(row=0, column=0)

        self.buttonReset = Button(self.buttonGame, width=15, text="Reset Game",
                                  state="disabled", command=self.gameReset)
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

    def gameAction(self):
        self.shortSel.config(state="disabled")
        self.longSel.config(state="disabled")
        self.buttonPlay.config(state="active")
        self.buttonReset.config(state="active")

        self.enableEntries()

    def gameReset(self):
        self.cleanEntries()
        self.disableEntries()

        self.gameType.set(None)

        self.shortSel.config(state="normal")
        self.longSel.config(state="normal")
        self.buttonPlay.config(state="disabled")
        self.buttonReset.config(state="disabled")

    def enableEntries(self):
        if self.gameType.get() == "short":
            self.shortEntry01.config(state="normal")
            self.shortEntry02.config(state="normal")
            self.shortEntry03.config(state="normal")
            self.shortEntry04.config(state="normal")
            self.shortEntry05.config(state="normal")
            self.shortEntry06.config(state="normal")
        else:
            self.longEntry11.config(state="normal")
            self.longEntry12.config(state="normal")
            self.longEntry13.config(state="normal")
            self.longEntry14.config(state="normal")
            self.longEntry15.config(state="normal")
            self.longEntry16.config(state="normal")

            self.longEntry21.config(state="normal")
            self.longEntry22.config(state="normal")
            self.longEntry23.config(state="normal")
            self.longEntry24.config(state="normal")
            self.longEntry25.config(state="normal")
            self.longEntry26.config(state="normal")

            self.longEntry31.config(state="normal")
            self.longEntry32.config(state="normal")
            self.longEntry33.config(state="normal")
            self.longEntry34.config(state="normal")
            self.longEntry35.config(state="normal")
            self.longEntry36.config(state="normal")

    def disableEntries(self):
        if self.gameType.get() == "short":
            self.shortEntry01.config(state="readonly")
            self.shortEntry02.config(state="readonly")
            self.shortEntry03.config(state="readonly")
            self.shortEntry04.config(state="readonly")
            self.shortEntry05.config(state="readonly")
            self.shortEntry06.config(state="readonly")
        else:
            self.longEntry11.config(state="readonly")
            self.longEntry12.config(state="readonly")
            self.longEntry13.config(state="readonly")
            self.longEntry14.config(state="readonly")
            self.longEntry15.config(state="readonly")
            self.longEntry16.config(state="readonly")

            self.longEntry21.config(state="readonly")
            self.longEntry22.config(state="readonly")
            self.longEntry23.config(state="readonly")
            self.longEntry24.config(state="readonly")
            self.longEntry25.config(state="readonly")
            self.longEntry26.config(state="readonly")

            self.longEntry31.config(state="readonly")
            self.longEntry32.config(state="readonly")
            self.longEntry33.config(state="readonly")
            self.longEntry34.config(state="readonly")
            self.longEntry35.config(state="readonly")
            self.longEntry36.config(state="readonly")

    def cleanEntries(self):
        if self.gameType.get() == "short":
            self.shortEntry01.delete(0, "end")
            self.shortEntry02.delete(0, "end")
            self.shortEntry03.delete(0, "end")
            self.shortEntry04.delete(0, "end")
            self.shortEntry05.delete(0, "end")
            self.shortEntry06.delete(0, "end")
        else:
            self.longEntry11.delete(0, "end")
            self.longEntry12.delete(0, "end")
            self.longEntry13.delete(0, "end")
            self.longEntry14.delete(0, "end")
            self.longEntry15.delete(0, "end")
            self.longEntry16.delete(0, "end")

            self.longEntry21.delete(0, "end")
            self.longEntry22.delete(0, "end")
            self.longEntry23.delete(0, "end")
            self.longEntry24.delete(0, "end")
            self.longEntry25.delete(0, "end")
            self.longEntry26.delete(0, "end")

            self.longEntry31.delete(0, "end")
            self.longEntry32.delete(0, "end")
            self.longEntry33.delete(0, "end")
            self.longEntry34.delete(0, "end")
            self.longEntry35.delete(0, "end")
            self.longEntry36.delete(0, "end")
