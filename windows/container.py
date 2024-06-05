from tkinter import Tk, Frame, LabelFrame, Radiobutton
from tkinter import StringVar


class GNumber(Tk):
    def __init__(self):
        super().__init__()
        self.build()
        self.selectMode()
        self.selectType()

    def build(self):
        self.title("G-Numbers - Main Menu")
        self.geometry("600x600")
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

        self.typeRadioShort = Radiobutton(typeGameFrame, text="Short",
                                          value="short",
                                          variable=self.typeGame,
                                          command=self.justAtest)
        self.typeRadioShort.grid(row=0, column=0)

        self.typeRadioReLong = Radiobutton(typeGameFrame, text="Long",
                                           value="long",
                                           variable=self.typeGame,
                                           command=self.justAtest)
        self.typeRadioReLong.grid(row=0, column=1)

    def justAtest(self):
        print(f"Mode Game: {self.modeGame.get()}")
        print(f"Type Game: {self.typeGame.get()}")
