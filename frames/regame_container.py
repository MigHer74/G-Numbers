from tkinter import Toplevel, Frame, LabelFrame, Radiobutton, Button
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
        self.panelOne.grid(row=0, column=0, padx=(15, 10), pady=(15, 0))

        self.replayGame = LabelFrame(self.panelOne, text=" Replay Game ",
                                     labelanchor="n")
        self.replayGame.grid(row=0, column=0)

        self.replayShort = Radiobutton(self.replayGame, text="Short Game",
                                       value="short", variable=self.replayType)
        self.replayShort.grid(row=0, column=0, padx=(10, 10), pady=(10, 0))

        self.replayLong = Radiobutton(self.replayGame, text="Long Game",
                                      value="long", variable=self.replayType)
        self.replayLong.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        self.replayButton = Frame(self)
        self.replayButton.grid(row=1, column=0, padx=(15, 10), pady=(15, 15))

        self.playButton = Button(self.replayButton, width=15, text="Play",
                                 state="disabled")
        self.playButton.grid(row=0, column=0, pady=(10, 0))

        self.newButton = Button(self.replayButton, width=15, text="New",
                                state="disabled")
        self.newButton.grid(row=1, column=0, pady=(10, 0))

        self.closeButton = Button(self.replayButton, width=15, text="Close",
                                  command=self.destroy)
        self.closeButton.grid(row=2, column=0, pady=(10, 10))
