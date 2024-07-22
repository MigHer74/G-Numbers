from tkinter import Toplevel, Frame, LabelFrame, Radiobutton
from tkinter import StringVar


class RGPanel(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()

        self.replayType = StringVar()
        self.replayType.set(None)

        self.build()
        self.focus()

    def build(self):
        self.title("G-Numbers | Replay Game")
        self.resizable(False, False)

        self.panelOne = Frame(self)
        self.panelOne.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))

        self.replayGame = LabelFrame(self.panelOne, text=" Replay Game ",
                                     labelanchor="n")
        self.replayGame.grid(row=0, column=0)

        self.replayShort = Radiobutton(self.replayGame, text="Short Game",
                                       value="short", variable=self.replayType)
        self.replayShort.grid(row=0, column=0, padx=(10, 10), pady=(10, 0))

        self.replayLong = Radiobutton(self.replayGame, text="Long Game",
                                      value="long", variable=self.replayType)
        self.replayLong.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
