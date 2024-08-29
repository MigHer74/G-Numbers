from tkinter import Toplevel, Frame, LabelFrame, Entry, Label, Button
from tkinter import Radiobutton
import general_tools as gt


class LongView(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()
        self.loadData()
        self.longBuild()
        # self.updateLabels()

    def longBuild(self):
        self.title("G-Numbers | Data Long Game")
        self.resizable(False, False)

        self.titleFrame = LabelFrame(self)
        self.titleFrame.grid(row=0, column=0, columnspan=3,
                             padx=(15, 15), pady=(15, 0), sticky="we")

        self.titleLabel = Label(self.titleFrame, text="Saved Numbers")
        self.titleLabel.pack(pady=(5, 5))

        self.lblFrame1 = LabelFrame(self, width=215, height=143)
        self.lblFrame1.grid(row=1, column=0, padx=(15, 0), pady=(15, 0))
        self.lblFrame1.grid_propagate(False)

        self.radio1 = Radiobutton(self.lblFrame1, text="Week #1")
        self.radio1.grid(row=0, column=0, pady=(10, 0))

        Label(self.lblFrame1, text=self.label11).grid(row=1, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame1, text=self.label12).grid(row=2, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame1, text=self.label13).grid(row=3, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 10),
                                                      sticky="w")

        self.lblFrame2 = LabelFrame(self, width=215, height=143)
        self.lblFrame2.grid(row=1, column=1, padx=(15, 0), pady=(15, 0))
        self.lblFrame2.grid_propagate(False)

        self.radio2 = Radiobutton(self.lblFrame2, text="Week #2")
        self.radio2.grid(row=0, column=0, pady=(10, 0))

        Label(self.lblFrame2, text=self.label21).grid(row=1, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame2, text=self.label22).grid(row=2, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame2, text=self.label23).grid(row=3, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 10),
                                                      sticky="w")

        self.lblFrame3 = LabelFrame(self, width=215, height=143)
        self.lblFrame3.grid(row=1, column=2, padx=(15, 15), pady=(15, 0))
        self.lblFrame3.grid_propagate(False)

        self.radio3 = Radiobutton(self.lblFrame3, text="Week #3")
        self.radio3.grid(row=0, column=0, pady=(10, 0))

        Label(self.lblFrame3, text=self.label31).grid(row=1, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame3, text=self.label32).grid(row=2, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame3, text=self.label33).grid(row=3, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 10),
                                                      sticky="w")

        self.lblFrame4 = LabelFrame(self, width=215, height=143)
        self.lblFrame4.grid(row=2, column=0, padx=(15, 0), pady=(15, 15))
        self.lblFrame4.grid_propagate(False)

        self.radio4 = Radiobutton(self.lblFrame4, text="Week #4")
        self.radio4.grid(row=0, column=0, pady=(10, 0))

        Label(self.lblFrame4, text=self.label41).grid(row=1, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame4, text=self.label42).grid(row=2, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame4, text=self.label43).grid(row=3, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 10),
                                                      sticky="w")

        self.lblFrame5 = LabelFrame(self, width=215, height=143)
        self.lblFrame5.grid(row=2, column=1, padx=(15, 0), pady=(15, 15))
        self.lblFrame5.grid_propagate(False)

        self.radio5 = Radiobutton(self.lblFrame5, text="Week #5")
        self.radio5.grid(row=0, column=0, pady=(10, 0))

        Label(self.lblFrame5, text=self.label51).grid(row=1, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame5, text=self.label52).grid(row=2, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame5, text=self.label53).grid(row=3, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 10),
                                                      sticky="w")

        self.lblFrame6 = LabelFrame(self, width=215, height=143)
        self.lblFrame6.grid(row=2, column=2, padx=(15, 15), pady=(15, 15))
        self.lblFrame6.grid_propagate(False)

        self.radio6 = Radiobutton(self.lblFrame6, text="Week #6")
        self.radio6.grid(row=0, column=0, pady=(10, 0))

        Label(self.lblFrame6, text=self.label61).grid(row=1, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame6, text=self.label62).grid(row=2, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 0), sticky="w")
        Label(self.lblFrame6, text=self.label63).grid(row=3, column=0,
                                                      padx=(10, 10),
                                                      pady=(10, 10),
                                                      sticky="w")

    def loadData(self):
        (self.week1Game1, self.week1Game2,
         self.week1Game3) = gt.load_weeks("long", "W1")

        (self.week2Game1, self.week2Game2,
         self.week2Game3) = gt.load_weeks("long", "W2")

        (self.week3Game1, self.week3Game2,
         self.week3Game3) = gt.load_weeks("long", "W3")

        (self.week4Game1, self.week4Game2,
         self.week4Game3) = gt.load_weeks("long", "W4")

        (self.week5Game1, self.week5Game2,
         self.week5Game3) = gt.load_weeks("long", "W5")

        (self.week6Game1, self.week6Game2,
         self.week6Game3) = gt.load_weeks("long", "W6")

        self.label11 = f"Game #1  --->  {self.week1Game1}"
        self.label12 = f"Game #2  --->  {self.week1Game2}"
        self.label13 = f"Game #3  --->  {self.week1Game3}"

        self.label21 = f"Game #1  --->  {self.week2Game1}"
        self.label22 = f"Game #2  --->  {self.week2Game2}"
        self.label23 = f"Game #3  --->  {self.week2Game3}"

        self.label31 = f"Game #1  --->  {self.week3Game1}"
        self.label32 = f"Game #2  --->  {self.week3Game2}"
        self.label33 = f"Game #3  --->  {self.week3Game3}"

        self.label41 = f"Game #1  --->  {self.week4Game1}"
        self.label42 = f"Game #2  --->  {self.week4Game2}"
        self.label43 = f"Game #3  --->  {self.week4Game3}"

        self.label51 = f"Game #1  --->  {self.week5Game1}"
        self.label52 = f"Game #2  --->  {self.week5Game2}"
        self.label53 = f"Game #3  --->  {self.week5Game3}"

        self.label61 = f"Game #1  --->  {self.week6Game1}"
        self.label62 = f"Game #2  --->  {self.week6Game2}"
        self.label63 = f"Game #3  --->  {self.week6Game3}"
