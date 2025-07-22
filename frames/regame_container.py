from tkinter import Toplevel, Frame, LabelFrame, Radiobutton, Button, Label
from tkinter import StringVar
from general_tools import center_window
import game_engine as gen


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
        center_window(self, 479, 271)
        self.resizable(False, False)

        self.panelOne = Frame(self)
        self.panelOne.grid(row=0, column=0, padx=(15, 10), pady=(15, 0))

        self.replayGame = LabelFrame(self.panelOne, text=" Replay Game ",
                                     labelanchor="n")
        self.replayGame.grid(row=0, column=0)

        self.replayShort = Radiobutton(self.replayGame, text="Short Game",
                                       value="short", variable=self.replayType,
                                       command=self.actionGame)
        self.replayShort.grid(row=0, column=0, padx=(10, 10), pady=(10, 0))

        self.replayLong = Radiobutton(self.replayGame, text="Long Game",
                                      value="long", variable=self.replayType,
                                      command=self.actionGame)
        self.replayLong.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        self.panelTwo = Frame(self)
        self.panelTwo.grid(row=1, column=0, columnspan=2, pady=(15, 15))

        self.newButton = Button(self.panelTwo, width=15, text="New",
                                state="disabled", command=self.newGame)
        self.newButton.grid(row=0, column=0, padx=(0, 15), pady=(10, 0))

        self.closeButton = Button(self.panelTwo, width=15, text="Close",
                                  command=self.destroy)
        self.closeButton.grid(row=0, column=1, padx=(15, 0), pady=(10, 0))

        self.panelThree = Frame(self)
        self.panelThree.grid(row=0, column=1)

        self.panelResults = LabelFrame(self.panelThree, width=310, height=180,
                                       text=" Numbers Repetition ",
                                       labelanchor="n")
        self.panelResults.grid(row=0, column=0, padx=(15, 15), pady=(15, 0))
        self.panelResults.grid_propagate(False)

    def actionGame(self):
        self.replayShort.config(state="disabled")
        self.replayLong.config(state="disabled")
        self.newButton.config(state="normal")

        (listResult1, listResult2, listResult3,
         listResult4, listFinal) = gen.gEngine(self.replayType.get())

        if self.replayType.get() == "short":
            result1 = f"5+ -> {", ".join(listResult1)}"
            result2 = f"4 --> {", ".join(listResult2)}"
            result3 = f"3 --> {", ".join(listResult3)}"
            result4 = f"2 --> {", ".join(listResult4)}"
            resultf = f"Final: {", ".join(listFinal)}"
        else:
            result1 = f"6+--> {", ".join(listResult1)}"
            result2 = f"5 ---> {", ".join(listResult2)}"
            result3 = f"4 ---> {", ".join(listResult3)}"
            result4 = f"3 ---> {", ".join(listResult4)}"
            resultf = f"Final: {", ".join(listFinal)}"

        self.labelRow01 = Label(self.panelResults, text=result1)
        self.labelRow01.grid(row=0, column=0, padx=10, pady=(5, 0),
                             sticky="w")

        self.labelRow02 = Label(self.panelResults, text=result2)
        self.labelRow02.grid(row=1, column=0, padx=10, pady=(10, 0),
                             sticky="w")

        self.labelRow03 = Label(self.panelResults, text=result3)
        self.labelRow03.grid(row=2, column=0, padx=10, pady=(10, 0),
                             sticky="w")

        self.labelRow04 = Label(self.panelResults, text=result4)
        self.labelRow04.grid(row=3, column=0, padx=10, pady=(10, 0),
                             sticky="w")

        self.labelRowF = Label(self.panelResults, text=resultf)
        self.labelRowF.grid(row=4, column=0, padx=10, pady=(10, 10),
                            sticky="w")

    def newGame(self):
        self.replayType.set(None)

        self.replayShort.config(state="normal")
        self.replayLong.config(state="normal")
        self.newButton.config(state="disabled")

        self.labelRow01.destroy()
        self.labelRow02.destroy()
        self.labelRow03.destroy()
        self.labelRow04.destroy()
        self.labelRowF.destroy()
