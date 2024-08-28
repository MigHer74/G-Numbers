from tkinter import Toplevel, Frame, LabelFrame, Entry, Label, Button
from tkinter import Radiobutton


class LongView(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()
        self.longBuild()

    def longBuild(self):
        self.title("G-Numbers | Data Long Game")
        self.resizable(False, False)

        self.lblFrame1 = LabelFrame(self)
        self.lblFrame1.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))

        self.radioOne = Radiobutton(self.lblFrame1, text="Week #1")
        self.radioOne.grid(row=0, column=0, padx=(15, 0), pady=(10, 0))

        self.label11 = Label(self.lblFrame1, text="Game #1:")
        self.label11.grid(row=1, column=0, padx=(38, 0), pady=(10, 0))

        self.label12 = Label(self.lblFrame1, text="Game #2:")
        self.label12.grid(row=2, column=0, padx=(38, 0), pady=(10, 0))

        self.label13 = Label(self.lblFrame1, text="Game #3:")
        self.label13.grid(row=3, column=0, padx=(38, 0), pady=(10, 10))

        self.lblFrame2 = LabelFrame(self)
        self.lblFrame2.grid(row=0, column=1, padx=(15, 0), pady=(15, 0))

        self.radio2 = Radiobutton(self.lblFrame2, text="Week #2")
        self.radio2.grid(row=0, column=0, padx=(15, 0), pady=(10, 0))

        self.label21 = Label(self.lblFrame2, text="Game #1:")
        self.label21.grid(row=1, column=0, padx=(38, 0), pady=(10, 0))

        self.label22 = Label(self.lblFrame2, text="Game #2:")
        self.label22.grid(row=2, column=0, padx=(38, 0), pady=(10, 0))

        self.label23 = Label(self.lblFrame2, text="Game #3:")
        self.label23.grid(row=3, column=0, padx=(38, 0), pady=(10, 10))

        self.lblFrame3 = LabelFrame(self)
        self.lblFrame3.grid(row=0, column=2, padx=(15, 15), pady=(15, 0))

        self.radio3 = Radiobutton(self.lblFrame3, text="Week #3")
        self.radio3.grid(row=0, column=0, padx=(15, 0), pady=(10, 0))

        self.label31 = Label(self.lblFrame3, text="Game #1:")
        self.label31.grid(row=1, column=0, padx=(38, 0), pady=(10, 0))

        self.label32 = Label(self.lblFrame3, text="Game #2:")
        self.label32.grid(row=2, column=0, padx=(38, 0), pady=(10, 0))

        self.label33 = Label(self.lblFrame3, text="Game #3:")
        self.label33.grid(row=3, column=0, padx=(38, 0), pady=(10, 10))

        self.lblFrame4 = LabelFrame(self)
        self.lblFrame4.grid(row=1, column=0, padx=(15, 0), pady=(15, 15))

        self.radio4 = Radiobutton(self.lblFrame4, text="Week #4")
        self.radio4.grid(row=0, column=0, padx=(15, 0), pady=(10, 0))

        self.label41 = Label(self.lblFrame4, text="Game #1:")
        self.label41.grid(row=1, column=0, padx=(38, 0), pady=(10, 0))

        self.label42 = Label(self.lblFrame4, text="Game #2:")
        self.label42.grid(row=2, column=0, padx=(38, 0), pady=(10, 0))

        self.label43 = Label(self.lblFrame4, text="Game #3:")
        self.label43.grid(row=3, column=0, padx=(38, 0), pady=(10, 10))

        self.lblFrame5 = LabelFrame(self)
        self.lblFrame5.grid(row=1, column=1, padx=(15, 0), pady=(15, 15))

        self.radio5 = Radiobutton(self.lblFrame5, text="Week #5")
        self.radio5.grid(row=0, column=0, padx=(15, 0), pady=(10, 0))

        self.label51 = Label(self.lblFrame5, text="Game #1:")
        self.label51.grid(row=1, column=0, padx=(38, 0), pady=(10, 0))

        self.label52 = Label(self.lblFrame5, text="Game #2:")
        self.label52.grid(row=2, column=0, padx=(38, 0), pady=(10, 0))

        self.label53 = Label(self.lblFrame5, text="Game #3:")
        self.label53.grid(row=3, column=0, padx=(38, 0), pady=(10, 10))

        self.lblFrame6 = LabelFrame(self)
        self.lblFrame6.grid(row=1, column=2, padx=(15, 15), pady=(15, 15))

        self.radio6 = Radiobutton(self.lblFrame6, text="Week #6")
        self.radio6.grid(row=0, column=0, padx=(15, 0), pady=(10, 0))

        self.label61 = Label(self.lblFrame6, text="Game #1:")
        self.label61.grid(row=1, column=0, padx=(38, 0), pady=(10, 0))

        self.label62 = Label(self.lblFrame6, text="Game #2:")
        self.label62.grid(row=2, column=0, padx=(38, 0), pady=(10, 0))

        self.label63 = Label(self.lblFrame6, text="Game #3:")
        self.label63.grid(row=3, column=0, padx=(38, 0), pady=(10, 10))
