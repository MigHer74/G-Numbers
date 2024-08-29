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

        self.lblFrame1 = LabelFrame(self)
        self.lblFrame1.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))

        self.radioOne = Radiobutton(self.lblFrame1, text="Week #1")
        self.radioOne.grid(row=0, column=0, pady=(10, 0))

        Label(self.lblFrame1, text=self.label11).grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="w")
        Label(self.lblFrame1, text=self.label12).grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="w")
        Label(self.lblFrame1, text=self.label13).grid(row=3, column=0, padx=(10, 10), pady=(10, 10),sticky="w")

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
