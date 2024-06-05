from tkinter import Tk, Frame, LabelFrame, Label, Entry, Radiobutton
from tkinter import StringVar


class GNumber(Tk):
    def __init__(self):
        super().__init__()
        self.build()
        self.selectMode()
        self.selectType()
        self.numbersPanel()

    def build(self):
        self.title("G-Numbers - Main Menu")
        self.resizable(False, False)

        self.appFrame = Frame(self)
        self.appFrame.pack()

    def selectMode(self):
        self.modeGame = StringVar()
        self.modeGame.set(None)

        modeGameFrame = LabelFrame(self.appFrame, text=" Select Mode")
        modeGameFrame.grid(row=0, column=0)

        self.modeRadioPlay = Radiobutton(modeGameFrame, text="Play Game",
                                         value="play",
                                         variable=self.modeGame,
                                         command=self.justAtest)
        self.modeRadioPlay.grid(row=0, column=0)

        self.modeRadioRePlay = Radiobutton(modeGameFrame, text="RePlay Game",
                                           value="replay",
                                           variable=self.modeGame,
                                           command=self.justAtest)
        self.modeRadioRePlay.grid(row=0, column=1)

    def selectType(self):
        self.typeGame = StringVar()
        self.typeGame.set(None)

        typeGameFrame = LabelFrame(self.appFrame, text=" Select Game")
        typeGameFrame.grid(row=0, column=1)

        self.typeRadioShort = Radiobutton(typeGameFrame, text="Short Game",
                                          value="short",
                                          variable=self.typeGame,
                                          command=self.justAtest)
        self.typeRadioShort.grid(row=0, column=0)

        self.typeRadioReLong = Radiobutton(typeGameFrame, text="Long Game",
                                           value="long",
                                           variable=self.typeGame,
                                           command=self.justAtest)
        self.typeRadioReLong.grid(row=0, column=1)

    def numbersPanel(self):
        numbersFrame = LabelFrame(self.appFrame, text=" Game Numbers ")
        numbersFrame.grid(row=2, column=0)

        gameOneLabel = Label(numbersFrame, text="Game #1")
        gameOneLabel.grid(row=0, column=0)

        self.gameOneEntry11 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=0, column=1)
        self.gameOneEntry12 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=0, column=2)
        self.gameOneEntry13 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=0, column=3)
        self.gameOneEntry14 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=0, column=4)
        self.gameOneEntry15 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=0, column=5)
        self.gameOneEntry16 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=0, column=6)

        gameTwoLabel = Label(numbersFrame, text="Game #2")
        gameTwoLabel.grid(row=1, column=0)

        self.gameTwoEntry21 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=1, column=1)
        self.gameTwoEntry22 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=1, column=2)
        self.gameTwoEntry23 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=1, column=3)
        self.gameTwoEntry24 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=1, column=4)
        self.gameTwoEntry25 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=1, column=5)
        self.gameTwoEntry26 = Entry(numbersFrame, width=3, justify="center",
                                    state="disabled").grid(row=1, column=6)

        gameThreeLabel = Label(numbersFrame, text="Game #3")
        gameThreeLabel.grid(row=2, column=0)

        self.gameThreeEntry31 = Entry(numbersFrame, width=3, justify="center",
                                      state="disabled").grid(row=2, column=1)
        self.gameThreeEntry32 = Entry(numbersFrame, width=3, justify="center",
                                      state="disabled").grid(row=2, column=2)
        self.gameThreeEntry33 = Entry(numbersFrame, width=3, justify="center",
                                      state="disabled").grid(row=2, column=3)
        self.gameThreeEntry34 = Entry(numbersFrame, width=3, justify="center",
                                      state="disabled").grid(row=2, column=4)
        self.gameThreeEntry35 = Entry(numbersFrame, width=3, justify="center",
                                      state="disabled").grid(row=2, column=5)
        self.gameThreeEntry36 = Entry(numbersFrame, width=3, justify="center",
                                      state="disabled").grid(row=2, column=6)

    def justAtest(self):
        print(f"Mode Game: {self.modeGame.get()}")
        print(f"Type Game: {self.typeGame.get()}")
